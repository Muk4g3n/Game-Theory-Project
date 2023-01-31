import {useState,useEffect} from 'react'
import Background from './images/Background.jpg'
import cardHolderBackground from './images/cardHolderBackground.jpg'
import BackCard from './images/BackCard.jpg'
import fire from './images/fire.png'
import metal from './images/metal.png'
import plant from './images/plant.png'
import stone from './images/stone.png'
import water from './images/water.png'
import lightning from './images/lightning.png'
import './App.css';

function App() {

  // const [data, setData] = useState({})

  // useEffect(()=>{
  //   fetch('/play')
  //   .then(res => res.json())
  //   .then(data =>{
  //     setData(data)
  //     console.log(data);
  //   })
  // },[])

  return (
    <div className="App">
      <div className='background'><img src={Background} alt='background'/></div>
      <div className='holder'>
        <h1 className='title' >Elemental Cards</h1>
        
        <div className='card-holder' >
          <img  src={cardHolderBackground} alt='background'/>
          <div className='machine' >
            <div className='card'>
              <img src={BackCard} alt='back' />
               </div>
            <div className='card'  > <img src={BackCard} alt='back' /></div>
            <div className='card'> <img src={BackCard} alt='back' /></div>
            <div className='card'> <img src={BackCard} alt='back' /> </div>
            <div className='card'> <img src={BackCard} alt='back' /> </div>
            <div className='card'> <img src={BackCard} alt='back' /> </div>
          </div>
          <div className='player' >
          <div className='card fire' onClick={()=>{
              console.log("hello");
              fetch('/play',{method:'POST',headers:{'Content-Type': 'application/json'},body:JSON.stringify({play:0})})
              .then()
            }} > <img src={fire} alt='back' /> </div>
            <div className='card water'> <img src={water} alt='back' /> </div>
            <div className='card stone'> <img src={stone} alt='back' /> </div>
            <div className='card metal'> <img src={metal} alt='back' /> </div>
            <div className='card light'> <img src={lightning} alt='back' /> </div>
            <div className='card plant'> <img src={plant} alt='back' /> </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
