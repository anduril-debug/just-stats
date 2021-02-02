import React from 'react';
import FormCircle from './FormCircle';
import LoadingFormCircle from './LoadingFormCircle';


const LastFiveForm = (props) => {

    if (props.form !== undefined) {
        return (

            <>
                {props.form.map(game => <FormCircle key={game['id']} letter={game['result']} />)}

            </>
        )
    } else {
        return (
            <>
                <LoadingFormCircle />
                <LoadingFormCircle />
                <LoadingFormCircle />
                <LoadingFormCircle />
                <LoadingFormCircle />
            </>
        )
    }

}


export default LastFiveForm;