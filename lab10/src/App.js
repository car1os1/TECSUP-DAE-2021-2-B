import React,{Component} from 'react';
import Layout from './components/layout';
import Productos from './components/Productos';
import Title from './components/Title';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      productos: []
    }
  }

  componentWillMount() {
    fetch('http://localhost:8000/api/productos')
      .then((response) => {
        return response.json()
      })
      .then((prod) => {
        this.setState({ productos: prod })
      })    
  } 

  render() {
    return(
      <Layout>
        <Title/>
        <Productos
        productos={this.state.productos}
        />
      </Layout>
    );
  }

}

export default App;
