import React, {useState} from "react";
import Footer from "../Component/footer";
import {Modal, Container, Row, Col, Button} from 'react-bootstrap'
import Map from "../Component/map";

function UnparPage() {
    const [state, setState] = useState(null);
  
    return (
      <div>
        <div className="title">
          PETA SEBARAN TOTAL PARTISIPAN PMDK UNPAR 2013-2018
        </div>
        <div className="map_container">
          <Map showTable={setState} />
        </div>
    </div>
    )
}

export default UnparPage;