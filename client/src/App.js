import Background from './images/Background.jpg'

import './App.css';
import Holder from './Holder';

function App() {

  

  return (
    <div className="App">
      <div className='background'><img src={Background} alt='background'/></div>
      <div className='holder'>
        <h1 className='title' >Elemental Cards</h1>
        <Holder/>
        
      </div>
    </div>
  );
}

export default App;
