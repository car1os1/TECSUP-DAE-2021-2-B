import  React,{Component} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';



class App extends Component{
  constructor(props){
    super(props)
    this.state ={
      aritulos:[
        {
          codigo:1,
          descripcion:'coca cola',
          precio:2.50
        },
        {
          codigo:2,
          descripcion:'fanta',
          precio:1.80
        },
      ]
    }
    this.borrar = this.borrar.bind(this);
  }
  render(){
    return(
      <div>
        <table class="table">
  <thead>
    <tr>
      <th scope="col">codigo</th>
      <th scope="col">descripcion</th>
      <th scope="col">precio</th>
      <th scope="col">borrar</th>
    </tr>
  </thead>
  <tbody>
  {this.state.aritulos.map(elemento=>{
              return(
                <tr key={elemento.codigo}>
                  <td>{elemento.codigo}</td>
                  <td>{elemento.descripcion}</td>
                  <td>{elemento.precio}</td>
                  <td>
                    <button onClick={()=>this.borrar(elemento.codigo)}>borrar</button>
                  </td>
                </tr>
              )
            })}
  </tbody>
</table>
</div>
    );
  }

  borrar(cod){
    var temp = this.state.aritulos.filter((el)=>el.codigo!==cod);
    this.setState({
      articulos:temp
    })
  }
}

export default App;