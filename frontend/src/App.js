import React, { Component } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container' 
import Table from 'react-bootstrap/Table'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form'                         


class App extends Component {
  constructor(props) {
      super(props);
      this.state =({
        prestamo:[],
        pos:null,
        titulo:'Nuevo',
        id:0,
        codigo:'',
        libro:'',
        fechainicio:'',
        fechafin:'',
        categoria:''
      })
      this.cambioLibro = this.cambioLibro.bind(this);
      this.cambioFechaInicio = this.cambioFechaInicio.bind(this);
      this.cambioFechaFin = this.cambioFechaFin.bind(this);
      this.cambiocategoria = this.cambiocategoria.bind(this);
      this.mostrar = this.mostrar.bind(this);
      this.eliminar = this.eliminar.bind(this);
      this.guardar = this.guardar.bind(this);
    
    }  
    componentDidMount(){
      axios.get('http://127.0.0.1:8000/prestamos')
      .then(res=> {
        this.setState({series:res.data})
      })
    }


    cambioLibro(e){
      this.setState({
        libro : e.target.value
      })
    }
  
    cambioFechaInicio(e){
      this.setState({
        fechainicio : e.target.value
      })
    }

    cambioFechaFin(e){
      this.setState({
        fechafin : e.target.value
      })
    }
  
  
    cambiocategoria(e){
      this.setState({
        categoria : e.target.value
      })
    }
  

    mostrar(cod,index){
      axios.get('http://127.0.0.1:8000/prestamos'+cod)
      .then(res => {
        this.setState({
          pos: index,
          titulo: 'Editar',
          id: res.data.id,
          libro :res.data.name,
          fechainicio: res.data.release_date,
          fechafin: res.data.release_date,
          categoria : res.data.category
        })
      })
    }
  
    guardar(e){
      e.preventDefault();
      let cod = this.state.id;
      const datos = {
        libro: this.state.nombre,
        fechainicio: this.state.fecha,
        fechafin: this.state.fecha,
        category: this.state.categoria
      }
      if(cod>0){
        //edición de un registro
        axios.put('http://127.0.0.1:8000/prestamos'+cod,datos)
        .then(res =>{
          let indx = this.state.pos;
          this.state.prestamo[indx] = res.data;
          var temp = this.state.prestamos;
          this.setState({
            pos:null,
            titulo:'Nuevo',
            id:0,
            libro:'',
            fechainicio:'',
            fechafin:'',
            categoria:'',
            prestamos: temp
          });
        }).catch((error) =>{
          console.log(error.toString());
        });
      }else{
        //nuevo registro
        axios.post('http://127.0.0.1:8000/prestamos',datos)
        .then(res => {
          this.state.series.push(res.data);
          var temp = this.state.series;
          this.setState({
            id:0,
            libro:'',
            fechainicio: '',
            fechafin: '',
            categoria:'',
            prestamos:temp
          });
        }).catch((error)=>{
          console.log(error.toString());
        });
      }
    }
  
    eliminar(cod){
      let rpta = window.confirm("Desea Eliminar?");
      if(rpta){
        axios.delete('http://127.0.0.1:8000/prestamos'+cod)
        .then(res =>{
          var temp = this.state.prestamos.filter((prestamo)=>prestamo.id !== cod);
          this.setState({
            prestamos: temp
          })
        })
      }
    }
  

  render() {
    return (<div>
      <Container>
          <Table striped bordered hover variant="dark">
          <thead>
            <tr>
              <th>nombre del libro</th>
              <th>Fecha de prestamo</th>
              <th>fecha de devolucion</th>
              <th>Categoria</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {this.state.prestamo.map((prestamo,index) =>{
              return (
                <tr key={prestamo.id}>
                  <td>{prestamo.libro}</td>
                  <td>{prestamo.fechapre}</td>
                  <td>{prestamo.fechadev}</td>
                  <td>{prestamo.category}</td>
                  <td>
                  <Button variant="success" onClick={()=>this.mostrar(prestamo.id,index)}>Editar</Button>
                  <Button variant="danger" onClick={()=>this.eliminar(prestamo.id,index)}>Eliminar</Button>
                  </td>
                </tr>
              )
            })}
          </tbody>
        </Table>
        <hr />
        <h1>{this.state.titulo}</h1>
        <Form onSubmit={this.guardar}>
            <input type="hidden" value={this.state.id} />
            <Form.Group className="mb-3">
              <Form.Label>Nombre del libro</Form.Label>
              <Form.Control type="text" value={this.state.libro} onChange={this.cambioLibro} />
            </Form.Group>
            <Form.Group className="mb-3">
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Categoria</Form.Label>
              <Form.Control type="text" value={this.state.categoria} onChange={this.cambiocategoria} />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Fecha prestamo</Form.Label>
              <Form.Control type="date" value={this.state.fechainicio} onChange={this.cambioFechaInicio} />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Fecha de devolucion</Form.Label>
              <Form.Control type="date" value={this.state.fechafin} onChange={this.cambioFechaFin} />
            </Form.Group>
            <Button variant="primary" type="submit">
              Guardar
            </Button>
        </Form>
      </Container>

    </div>)
  }
}
export default App;

