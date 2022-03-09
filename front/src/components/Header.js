import React from 'react';
import Container from 'react-bootstrap/Container';
import { LinkContainer } from 'react-router-bootstrap';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown'

class Header extends React.Component{
    render() {
        return(
            <Navbar bg="light" expand="lg">
            <Container>
              <LinkContainer to="/">
                <Navbar.Brand>Moodle</Navbar.Brand>
              </LinkContainer>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">
                  <NavDropdown title="Materias" id="basic-  nav-dropdown">
                    <LinkContainer to="/Materias">
                      <NavDropdown.Item>Listar Materias</NavDropdown.Item>
                    </LinkContainer>
                    <LinkContainer to="/novaMateria">
                      <NavDropdown.Item>Nova Materia</NavDropdown.Item>
                    </LinkContainer>
                  </NavDropdown>
                </Nav>
              </Navbar.Collapse>
            </Container>
            </Navbar>
        );
    }
}
