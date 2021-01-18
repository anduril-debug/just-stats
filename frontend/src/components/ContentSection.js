import React from 'react';
import HotNews from './HotNews';
import News from './News';

function ContentSection() {
    return (
        <>
            <div className="col-9 test2">
                <HotNews />
                <News />
            </div>
        </>
    )
}

export default ContentSection;