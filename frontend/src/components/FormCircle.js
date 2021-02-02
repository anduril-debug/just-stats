import React from 'react';
import './FormCircle.css';


const FormCircle = (props) => {



    if (props.letter === "W") {
        return (
            <>
                <span className="circle win-circle">{props.letter}</span>
            </>
        )
    }
    else if (props.letter === "D") {
        return (
            <>
                <span className="circle draw-circle">{props.letter}</span>
            </>
        )
    }
    else {
        return (
            <>
                <span className="circle lose-circle">{props.letter}</span>
            </>
        )
    }



}


export default FormCircle;