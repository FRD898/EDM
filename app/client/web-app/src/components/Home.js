import { TextField, IconButton } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import { useEffect, useState } from "react";
import axios from "axios";
import SearchIcon from '@material-ui/icons/Search';
import Form from "./Form"


const useStyles = makeStyles((theme) => ({
  root: {
    //backgroundColor: "blue",
    padding: "40px",
  },
  table:{
    margin: 'auto',
    width: '50%',
    padding: '10px',
  },
  row: {
      backgroundColor: "#EEEEEE",
  },
  header:{
      backgroundColor: "black",
      color: "white",
  }
}));

export default function Home() {
  const [docList, setDocList] = useState([{
    Abstract: " ",
    Author: " ",
    ID: " ",
    "Publication Type": " ",
    Source: " ",
    Terms:
      " ",
    Title: " ",
    UI: " ",
    date: " "
  }]);
  const classes = useStyles();
  const [resultado, setResultado] = useState([])

  const ListadeAlumnos = resultado.map((item, index) => {
    return (
        <tr className={classes.row} key={index}>
            <td>Alumno {index}</td>
            <td>{item}</td>
        </tr>
    );
  });
  
  return (
    <div className={classes.root}>
      <div >
        <h1>Bienvenido</h1>
        <Form setRespuesta = {setResultado}></Form>
      </div>
      <div>
          <h2>Resultados de la predicción</h2>
          <table className={classes.table}>
            <tr className={classes.header}>
                <th>Alumno</th>
                <th>Resultado</th>
            </tr>
            <tbody>
                {ListadeAlumnos}
            </tbody>
          </table>
      </div>
    </div>)
}