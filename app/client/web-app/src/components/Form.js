import React, {useState} from 'react';
import axios from "axios";
import Papa from "papaparse";

export default function Form(param) {
    const [name, setName] = useState('');
    const [selectedFile, setSelectedFile] = useState({});
    const handleSubmit = (e) =>{
        e.preventDefault();
        axios.get('http://127.0.0.1:4000/search', {params: {
            data: JSON.stringify(selectedFile)
        }}
        ).then((response)=>{
            console.log(response.data.prediccion)
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
        <form onSubmit={handleSubmit}>
            <input
            type="file"
            onChange={handleFileInput}
            />
      </form>
    )
  }