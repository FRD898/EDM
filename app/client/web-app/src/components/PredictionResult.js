import { makeStyles } from "@mui/styles";
import { useEffect } from "react";
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


export default function PredictionResult(props){
    const classes = useStyles();
    const ListadeAlumnos = props.resultado.map((item, index) => {
        return (
            
            <tr className={item == "desaprobará" ? classes.red : classes.row} key={index}>
                <td>Alumno {index}</td>
                <td>{item}</td>
            </tr>
        );
    });
    return(
        <div>
          <h2>Resultados de la predicción</h2>
          <table className={classes.table}>
            <tbody>
                <tr className={classes.header}>
                    <th>Alumno</th>
                    <th>Resultado</th>
                </tr>
                {ListadeAlumnos}
            </tbody>
          </table>
        </div>
    )
}