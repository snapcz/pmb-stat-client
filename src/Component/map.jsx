/* Imports */
import React from "react";
import axios from "axios";
import * as am4core from "@amcharts/amcharts4/core";
import * as am4maps from "@amcharts/amcharts4/maps";
import am4geodata_data_countries2 from "@amcharts/amcharts4-geodata/data/countries2";
import am4themes_dark from "@amcharts/amcharts4/themes/dark";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import { useEffect } from "react";

am4core.useTheme(am4themes_animated);

function MapComp(props) {
  const showTable = props.showTable;
  const findVal = (obj, val) => {
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].properties.name === val) {
        return obj[i].id;
      }
    }
    return false;
  };

  useEffect(() => {
    
    const prepData = async () => {
      let currentMap = am4geodata_data_countries2["ID"]["maps"][1];
      let chart = am4core.create("chartdiv", am4maps.MapChart);
      console.log("https://www.amcharts.com/lib/4/geodata/json/" + currentMap + ".json")
      chart.geodataSource.url =
        "https://www.amcharts.com/lib/4/geodata/json/" + currentMap + ".json";

      chart.geodataSource.events.on("parseended", async function (ev) {
        let data_features = ev.target.data.features;
        console.log(data_features)
        const reqOne = axios.get(
          process.env.REACT_APP_API_URL + "/pmdk/all/province"
        );
        const reqTwo = axios.get(
          process.env.REACT_APP_API_URL + "/pmdk/2018/city_reg"
        );

        axios
          .all([reqOne, reqTwo])
          .then(
            axios.spread((...response) => {
              const provinceData = response[0];
              const cityData = response[1];
              // do something with provinceData
              let data = [];
              let max = 0;
              let min = Number.MAX_SAFE_INTEGER;
              for (const key in provinceData.data) {
                //if (min > provinceData.data[key].VALUE)
                min =
                  min > provinceData.data[key].VALUE
                    ? provinceData.data[key].VALUE
                    : min;
                //if (max < provinceData.data[key].VALUE)
                max =
                  max < provinceData.data[key].VALUE
                    ? provinceData.data[key].VALUE
                    : max;
                let check = findVal(data_features, key);
                if (check) {
                  data.push({
                    id: check,
                    value: provinceData.data[key].VALUE,
                    normalized: provinceData.data[key].NORMALIZED,
                  });
                }
              }
              polygonSeries.data = data;

              // Set up heat legend
              let heatLegend = chart.createChild(am4maps.HeatLegend);
              heatLegend.series = polygonSeries;
              heatLegend.align = "right";
              heatLegend.width = am4core.percent(25);
              heatLegend.marginRight = am4core.percent(9);
              heatLegend.minValue = 0;
              heatLegend.maxValue = max;

              // Set up custom heat map legend labels using axis ranges
              let minRange = heatLegend.valueAxis.axisRanges.create();
              minRange.value = heatLegend.minValue;
              minRange.label.text = min.toString();
              minRange.label.fill = am4core.color("#f7f7f7");
              let maxRange = heatLegend.valueAxis.axisRanges.create();
              maxRange.value = heatLegend.maxValue;
              maxRange.label.text = max.toString();
              maxRange.label.fill = am4core.color("#f7f7f7");

              // Blank out internal heat legend value axis labels
              heatLegend.valueAxis.renderer.labels.template.adapter.add(
                "text",
                function (labelText) {
                  return "";
                }
              );

              // do something with city data
              let city_data = [];
              for (const key in cityData.data) {
                city_data.push({
                  minZoomLevel: 3,
                  title: key,
                  latitude: cityData.data[key].latitude,
                  longitude: cityData.data[key].longitude,
                  total: cityData.data[key].total,
                  color: "rgba(" + cityData.data[key].color.toString() + ")",
                });
              }
              imageSeries.data = city_data;
            })
          )
          .catch((errors) => {
            // do something
          });
      });

      // Set projection
      chart.projection = new am4maps.projections.Mercator();

      // Create map polygon series
      let polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
      polygonSeries.mapPolygons.template.fill = am4core.color("#6e6e6e");

      // create map markers
      var imageSeries = chart.series.push(new am4maps.MapImageSeries());
      imageSeries.id = "markers";
      imageSeries.clickable = true;

      //Set min/max fill color for each area
      polygonSeries.heatRules.push({
        property: "fill",
        target: polygonSeries.mapPolygons.template,
        min: am4core.color("#f04337"),
        max: am4core.color("#210908"),
        logarithmic: true,
      });

      // Make map load polygon data (state shapes and names) from GeoJSON
      polygonSeries.useGeodata = true;

      // Configure series tooltip
      let polygonTemplate = polygonSeries.mapPolygons.template;
      polygonTemplate.tooltipText = "{name}: {value}";
      polygonTemplate.nonScalingStroke = true;
      polygonTemplate.strokeWidth = 0.5;

      // Create hover state and set alternative fill color
      let hs = polygonTemplate.states.create("hover");
      hs.properties.fill = am4core.color("#18a4c7");

      // create template
      let imageSeriesTemplate = imageSeries.mapImages.template;
      imageSeriesTemplate.propertyFields.latitude = "latitude";
      imageSeriesTemplate.propertyFields.longitude = "longitude";
      imageSeriesTemplate.propertyFields.title = "title";
      let circle = imageSeriesTemplate.createChild(am4core.Circle);
      circle.radius = 6;
      circle.propertyFields.fill = "color";
      circle.stroke = am4core.color("#FFFFFF");
      circle.strokeWidth = 2;
      circle.nonScaling = true;
      circle.tooltipText = "{title} : {total}";
      circle.id = "title";

      // zoom event
      const updateImageVisibility = (ev) => {
        var chart = ev.target.baseSprite;
        var series = chart.map.getKey("markers");
        series.mapImages.each(function (image) {
          if (image.dataItem.dataContext.minZoomLevel) {
            if (image.dataItem.dataContext.minZoomLevel >= chart.zoomLevel) {
              image.hide();
            } else {
              image.show();
            }
          }
        });
      };
      imageSeries.events.on("datavalidatednpm", updateImageVisibility);
      imageSeriesTemplate.events.on("doublehit", async (ev) => {
        let city = ev.target.dataItem.dataContext.title;
        axios
          .get(process.env.REACT_APP_API_URL + "/school_list/pmdk/2018/" + city)
          .then((response) => {
            console.log(response);
            showTable({
              data: response.data.data,
              city: city,
            });
          })
          .catch((error) => {
            console.log(error);
          });
      });
      chart.events.on("zoomlevelchanged", updateImageVisibility);
      //disable pan and drag
      // chart.seriesContainer.draggable = false;
      chart.seriesContainer.resizable = false;

      //disable zoom
      chart.maxZoomLevel = 5;
    };
    prepData();
  }, []);

  return (
    <>
      <div id="chartdiv" />
    </>
  );
}

export default MapComp;
