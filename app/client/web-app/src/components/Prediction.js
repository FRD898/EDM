import React, {useState} from 'react';
import axios from "axios";
import Papa from "papaparse";
import { Button, Paper } from "@mui/material";
import { makeStyles } from "@mui/styles";

const useStyles = makeStyles((theme) => ({
    button:{
        backgroundColor: "skyblue"
    }
  }));

export default function Form(param) {
    const classes = useStyles();
    const [name, setName] = useState('');
    const [selectedFile, setSelectedFile] = useState({});
    const handleSubmit = (e) =>{
        e.preventDefault();
        axios.get('http://127.0.0.1:4000/search', {params: {
            data: JSON.stringify(selectedFile)
        }}
        ).then((response)=>{
            console.log("pred",response.data.prediccion)
            console.log("real",response.data.real)
            param.setRespuesta(response.data.prediccion);
            if(response.status===200){
                console.log("OK")
            }else{
                console.error(response.status)
            }
        }).catch((error)=>{
            console.error(error)
        })    
    }

    const handleFileInput = (e) =>{  
        Papa.parse(e.target.files[0], {
            complete: function(results) {
            console.log("Finished:", results.data);
            setSelectedFile(results.data)
            }}
        )
        //setSelectedFile(file)


    }

    return (
        
        <Paper>
            <h2>Suba el archivo con los datos de los alumnos</h2>
            <input
                type="file"
                onChange={handleFileInput}
            />
            <Button className={classes.button} variant="contained" onClick={handleSubmit}>Submit</Button>
        </Paper>
    )
  }