import React from 'react';
import './FormCircle.css';


const FormCircle = (props) => {



    if (props.letter === "W") {
        return (
            <>
                <button className="circle win-circle" title={props.score}>{props.letter}</button>
            </>
        )
    }
    else if (props.letter === "D") {
        return (
            <>
                <button className="circle draw-circle" title={props.score}>{props.letter}</button>

            </>
        )
    }
    else {
        return (
            <>
                <button className="circle lose-circle" title={props.score}>{props.letter}</button>

            </>
        )
    }



}


export default FormCircle;