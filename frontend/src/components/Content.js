import React from 'react';
import './Content.css';
import Table from './Table';

function Content() {
    return (
        <div className='content row'>
            <div className="table-side col-3">
                <Table size='small' />
            </div>
            <div className="content-side col-9">
                <div className="hot-content">
                    some hot contnet
                </div>

                <div className="news">
                    news bitch
                </div>
            </div>


        </div>
    )
}


export default Content;