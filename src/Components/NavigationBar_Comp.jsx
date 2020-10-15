import React, { Component } from "react";
import {
  Navbar,
  Form,
  NavDropdown,
  Button,
  Nav,
  FormControl,
} from "react-bootstrap";

export default class NavBar extends Component {
  constructor(props) {
    super(props);
    console.log(props.halaman);

    this.state = {
      menu_link: "Alamat",
      tampilan_apa: "Navbar",
      input: "",

    };

    this.input = "Kosong"
  }

  checkState = () => {
    if (this.state.menu_link === "Alamat") return "Link";
    else return "Alamat";
  };

  gantiState = () => {
    this.setState({
      menu_link: this.state.menu_link === "Alamat" ? "Link" : "Alamat",
    });
  };

  gantiTampilan = () => {
      this.setState({
          tampilan_apa: this.state.tampilan_apa === "Navbar" ? "Text" : "Navbar"
      })
  }

  componentDidMount = () => {
      //get http request buat update state
  }

  componentWillUnmount = () => {
      window.alert("Comopnent now unmounting");
  }

  render() {
    return (
      <>
        <Button onClick={this.gantiTampilan}>
            Ganti Tampilan
        </Button>
        {this.state.tampilan_apa === "Navbar" ? (
          <Navbar bg="light" expand="lg">
            <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="mr-auto">
                <Nav.Link href="#home">Home</Nav.Link>
                <Nav.Link href="#link">{this.state.menu_link}</Nav.Link>
                <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                  <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.2">
                    Another action
                  </NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.3">
                    Something
                  </NavDropdown.Item>
                  <NavDropdown.Divider />
                  <NavDropdown.Item href="#action/3.4">
                    Separated link
                  </NavDropdown.Item>
                </NavDropdown>
              </Nav>
              <Form inline>
                <FormControl
                  type="text"
                  placeholder="Search"
                  className="mr-sm-2"
                />
                <Button onClick={this.gantiState} variant="outline-success">
                  Search
                </Button>
              </Form>
            </Navbar.Collapse>
          </Navbar>
        ) : (
          <div>Haiyoooo</div>
        )}
        <span><input onChange={(event) => {
            this.setState({input:event.target.value})
            //this.input = event.target.value
            //console.log(this.input)
            }
            } as="text"/><Button onClick={this.checkInput}>Check</Button></span>
        <div>Input anda: {this.state.input}</div>
        <div>
            {
                this.props.data.map((row)=>{
                    return <p>{row}</p>
                })
            }
        </div>
      </>
    );
  }
}
