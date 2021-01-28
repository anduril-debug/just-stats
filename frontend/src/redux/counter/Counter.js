import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { selectCount, increment, incrementByAmount, incrementAsync } from './counterSlice';


const Counter = () => {

    const count = useSelector(selectCount);
    const dispatch = useDispatch()

    return (
        <>
            Counter component
            { count}
            <button onClick={() => dispatch(increment())}>+</button>
            <button onClick={() => dispatch(incrementByAmount(5))}>by 5 +</button>
            <button onClick={() => dispatch(incrementAsync(125))}>ASYNCpm</button>
        </>
    );

}





export default Counter;