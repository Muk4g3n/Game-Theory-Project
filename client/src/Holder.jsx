import {useState,useEffect} from 'react'
import cardHolderBackground from './images/cardHolderBackground.jpg'
import fire from './images/fire.png'
import metal from './images/metal.png'
import plant from './images/plant.png'
import stone from './images/stone.png'
import water from './images/water.png'
import lightning from './images/lightning.png'

import './App.css';
import Card from './Card'
import PlayerCard from './PlayerCard'

function Holder() {
    // 0:fire, 1:water , 2:rock , 3:metal ,4:lighning ,5:plant ,
    let stratImg = [fire,water,stone,metal, lightning,plant]
    const [machineStrats, setMachineStrats] = useState([0,1,2,3,4,5])
    const [playerStrats, setPlayerStrats] = useState([0,1,2,3,4,5])

    

  useEffect(()=>{
    fetch('/play')
    .then(res => res.json())
    .then(data =>{
      console.log("I'm here")
      console.log(data); 
    })
  },[machineStrats])


    return ( <>
        <div className='card-holder' >
          <img  src={cardHolderBackground} alt='background'/>
          <div className='machine' >
                {
                    machineStrats.map((strats,i)=>{
                      return  <Card key={i} />
                    })
                }

            
            
          </div>
          <div className='player' >
          

                {
                    playerStrats.map((strat,i)=>{
                      return  <PlayerCard key={i} Element={stratImg[strat]} Strat={strat} />
                    })
                }




          </div>
        </div>
    </> );
}

export default Holder;