import { makeStyles } from "@mui/styles";
import { useEffect, useState } from "react";
import Bar from "./Bar"
import Prediction from "./Prediction"
import PredictionResult from "./PredictionResult";

const useStyles = makeStyles((theme) => ({
  root: {
    //backgroundColor: "blue",
    padding: "40px",
  },
  table:{
    margin: 'auto',
    width: '80%',
    padding: '10px',
  },
  row: {
      backgroundColor: "#EEEEEE",
  },
  red: {
    backgroundColor: "pink",
    },
  header:{
      backgroundColor: "black",
      color: "white",
  },
  logo:{
      height:"200px",
      width: "150px" 
  }
}));

export default function Home() {
  const [resultado, setResultado] = useState([])
  const classes = useStyles();
  
  return (
    <div className={classes.root}>
      <Bar></Bar>
      <div >
        <h1>Bienvenido</h1>
        <img className={classes.logo} src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Uni-logo_transparente_granate.png"></img>
        <Prediction setRespuesta = {setResultado}></Prediction>
      </div>
      <PredictionResult resultado={resultado}></PredictionResult>
    </div>)
}