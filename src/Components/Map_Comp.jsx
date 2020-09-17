/* Imports */
import React from "react";
import Axios from "axios";
import * as am4core from "@amcharts/amcharts4/core";
import * as am4maps from "@amcharts/amcharts4/maps";
import am4geodata_data_countries2 from "@amcharts/amcharts4-geodata/data/countries2";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import { useEffect } from "react";
/* Chart code */
// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end

function MapComp() {
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
      // calculate which map to be used
      let currentMap = am4geodata_data_countries2["ID"]["maps"][1];

      // get country title
      // let title = "";
      // if (am4geodata_data_countries2["ID"]["country"]) {
      //   title = am4geodata_data_countries2["ID"]["country"];
      // }

      // Create map instance
      let chart = am4core.create("chartdiv", am4maps.MapChart);

      // create title
      // chart.titles.create().text = title;

      // Set map definition OR as in another human language, map source (geoJSON)
      chart.geodataSource.url =
        "https://www.amcharts.com/lib/4/geodata/json/" + currentMap + ".json";
      chart.geodataSource.events.on("parseended", async function (ev) {
        let data_features = ev.target.data.features;
        await Axios({
          method: "GET",
          url: "http://127.0.0.1:5000/pmdk/all",
        }).then(function (res) {
          let data = []; //create random population data ? maybe place the axios get http req from localhost in here
          let max = 0;
          for (const key in res.data) {
            if (max < res.data[key].VALUE) max = res.data[key].VALUE;
            let check = findVal(data_features, key);
            if (check) {
              data.push({
                id: check,
                value: res.data[key].VALUE,
                normalized: res.data[key].NORMALIZED,
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
          minRange.label.text = "Little";
          minRange.label.fill = am4core.color('#cccccc');
          let maxRange = heatLegend.valueAxis.axisRanges.create();
          maxRange.value = heatLegend.maxValue;
          maxRange.label.text = "A lot!";
          maxRange.label.fill = am4core.color('#cccccc');

          // Blank out internal heat legend value axis labels
          heatLegend.valueAxis.renderer.labels.template.adapter.add(
            "text",
            function (labelText) {
              return "";
            }
          );
        });
      });

      // Set projection
      chart.projection = new am4maps.projections.Mercator();

      // Create map polygon series
      let polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());

      //Set min/max fill color for each area
      polygonSeries.heatRules.push({
        property: "fill",
        target: polygonSeries.mapPolygons.template,
        min: am4core.color("#f04337"),
        max: am4core.color("#42120f"),
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

      //disable pan and drag
      chart.seriesContainer.draggable = false;
      chart.seriesContainer.resizable = false;

      //disable zoom
      chart.maxZoomLevel = 1;
    };
    prepData();
  }, []);

  return <div id="chartdiv" style={{ width: "100%", height: "500px" }}></div>;
}

export default MapComp;
