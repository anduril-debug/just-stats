import React from 'react';


const LoadingTable = (props) => {

    const forMap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    if (props.size === "small") {
        return (
            <>
                <table id="main-table" className="table table-hover table-striped table-dark">
                    <thead className="table-head">
                        <tr>
                            <th className="position" scope="col">Position</th>
                            <th className="club" scope="col">Club</th>
                            <th className="points" scope="col">Points</th>

                        </tr>
                    </thead>
                    <tbody>
                        {forMap.map((index) =>
                            <tr key={index}>
                                <td className="position" ></td>
                                <td className="club"><span id="hidden-span">MANCHESTER UNITED</span> </td>
                                <td className="points"></td>
                            </tr>)}

                    </tbody>
                </table>
            </>
        )
    }

}


export default LoadingTable;