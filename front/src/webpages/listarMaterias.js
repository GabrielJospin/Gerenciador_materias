import React, { useEffect, useState } from 'react';
import api from "../services/api.js";
import Container from 'react-bootstrap/Container'
import ListGroup from 'react-bootstrap/ListGroup'


const ListarMaterias = () => {

  const [materia, setFunc] = useState([]);

  const fetchMaterias = () => {
    api
    .get("/Matters")
    .then((response) =>  setFunc(response.data))
    .catch((err) => {
      console.error("ops! ocorreu um erro" + err);
    });
  }

  useEffect(fetchMaterias, []);

  if (!materia) return null;

  return(
    <div>
      <div style={{display: 'flex', justifyContent: 'center', marginTop: '15px'}}>
        <h1 style={{width: '90vw'}}>Materias</h1>
      </div>
      <div style={{display: 'flex', justifyContent: 'center', marginTop: '15px'}}>
        <div style={{width: '90vw', marginBottom: '15px'}}>
          <Container>
              <ListGroup>
                  {materia.map(materia =>
                      <ListGroup.Item>
                          <h1 color={materia.color_hex} >{materia.name} - {materia.code}</h1>
                          <p>
                              Ministrada por: {materia.teacher} <br/>
                              Pertence ao Semestre: {materia.semester} <br/>
                              {materia.description} <br/>
                              <a href={materia.page}>Acessar {materia.name}</a>
                          </p>
                      </ListGroup.Item>
                  )}
              </ListGroup>
          </Container>
        </div>
      </div>
    </div>
  );
}

export default ListarMaterias;