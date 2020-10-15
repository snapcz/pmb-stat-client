import React, { useState, useEffect } from "react";
import { ResponsiveLine } from "@nivo/line";
import Axios from "axios";
import { Spinner } from "react-bootstrap";

function Trends(props) { //using nivo
  const { jalur, tipe, detail } = props;
  const [state, setState] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      await Axios({
        method: "get",
        url: "/pmdk/trend",
        baseURL: process.env.REACT_APP_API_URL,
        params: {
          jalur: jalur,
          tipe: tipe,
          detail: detail ? detail : null,
        },
      })
        .then(function (response) {
          let data = [];
          for (const key in response.data) {
            data.push({
              x: key,
              y: response.data[key].TOTAL,
            });
          }
          setState([
            {
              id: jalur,
              data: data,
            },
          ]);
        })
        .catch(function (error) {
          console.log(error);
        });
    };

    fetchData();
  }, []);

  return (
    <>
      {state ? (
        <ResponsiveLine
          data={state}
          margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
          xScale={{ type: "point" }}
          yScale={{
            type: "linear",
            min: "auto",
            max: "auto",
            reverse: false,
          }}
          axisTop={null}
          axisRight={null}
          axisBottom={{
            orient: "bottom",
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "Tahun",
            legendOffset: 36,
            legendPosition: "middle",
          }}
          axisLeft={{
            orient: "left",
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "Total Partisipan",
            legendOffset: -45,
            legendPosition: "middle",
          }}
          colors={{ scheme: "nivo" }}
          pointSize={10}
          pointColor={{ theme: "background" }}
          pointBorderWidth={2}
          pointBorderColor={{ from: "serieColor" }}
          pointLabel="y"
          pointLabelYOffset={-12}
          enableArea={true}
          useMesh={true}
          legends={[
            {
              anchor: "bottom-right",
              direction: "column",
              justify: false,
              translateX: 100,
              translateY: 0,
              itemsSpacing: 0,
              itemDirection: "left-to-right",
              itemWidth: 80,
              itemHeight: 20,
              itemOpacity: 0.75,
              symbolSize: 12,
              symbolShape: "circle",
              symbolBorderColor: "rgba(0, 0, 0, .5)",
              effects: [
                {
                  on: "hover",
                  style: {
                    itemBackground: "rgba(0, 0, 0, .03)",
                    itemOpacity: 1,
                  },
                },
              ],
            },
          ]}
        />
      ) : (
        <Spinner variant="primary" animation="border" />
      )}
    </>
  );
}

export default Trends;
