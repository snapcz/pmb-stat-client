import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import Map from "./Components/Map_Comp";
import NavBar from "./Components/NavigationBar_Comp";
import { Button } from "react-bootstrap";
import Table from "./Components/Table_Comp";
import TableMT from "./Components/TableMT_Comp";
import Trends from "./Components/Trends_NivoComp";

function App() {
  const [state, setState] = useState(null);

  const unmountNavbar = () => {
    console.log(state);
    console.log("test");
    setState(0);
  };

  return (
    <div className="App">
      {/* {
        state > 0 && <NavBar data={[1,2,3,4,5]} state={state}/>
      }
      <Button onClick={unmountNavbar}>Test</Button> */}
      <div className="title">
        PETA SEBARAN TOTAL PARTISIPAN PMDK UNPAR 2013-2018
      </div>
      <div className="map_container">
        <Map showTable={setState} />
      </div>
      <div className="tableContainer">
        {state && (
          <>
            <div>
              <h3>Detail partisipan diseluruh {state.city}</h3>
            </div>
            {/* <Table /> */}
            <TableMT data={state.data}/>
          </>
        )}
      </div>
      <div style={{width:'1100px',height:'500px'}}>
        <Trends jalur={'pmdk'} tipe={'all'} />
      </div>
    </div>
  );
}

export default App;
