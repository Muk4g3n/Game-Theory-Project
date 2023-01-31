import { useRef } from 'react';
import {useState,useEffect} from 'react'


function PlayerCard({Element,Strat}) {
    const [chosenStrat, setChosenStrat] = useState(undefined)
    const cardRef = useRef(0)
    useEffect(() => {
        if (chosenStrat) {
          fetch("/play", {
            method: "POST",
            body: JSON.stringify({"strat":chosenStrat}),
            headers: { "content-type": "application/json","Access-Control-Allow-Origin":"*","Access-Control-Allow-Headers": "*","Access-Control-Allow-Methods": "*"},
          })
            .then((res) => {
              if (!res.ok) return Promise.reject(res);
              return res.json();
            })
            .then((data) => {
              // console.log(data);
              cardRef.current.style.opacity="0.2"
              cardRef.current.style.pointerEvents = "none";
            })
            .catch(console.error);
        }
      }, [chosenStrat]);

    return ( <>
        <div className='card water' ref={cardRef} onClick={()=> {setChosenStrat(Strat);
            
            }} > <img src={Element} alt='back' /> </div>
    </> );
}

export default PlayerCard;