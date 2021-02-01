import React, { } from 'react';
import './Table.css';
import { teamsSelector } from '../redux/teams/teamsSlice';
import { useSelector } from 'react-redux';



function Table() {

    const { isLoading, hasError, teams } = useSelector(teamsSelector)



    if (isLoading) return <p>Loading....</p>
    if (hasError) return <p>something went wrong...</p>










    return (
        <>

            <h3>hello</h3>
            <table id="main-table" className="table table-hover table-striped table-dark">
                <thead className="table-head">
                    <tr>
                        <th className="position" scope="col">Position</th>
                        <th className="club" scope="col">Club</th>
                        <th className="played" scope="col">Played</th>
                        <th className="won" scope="col">Won</th>
                        <th className="drawn" scope="col">Drawn</th>
                        <th className="lost" scope="col">Lost</th>
                        <th className="gf" scope="col">GF</th>
                        <th className="ga" scope="col">GA</th>
                        <th className="gd" scope="col">GD</th>
                        <th className="points" scope="col">Points</th>
                        <th className="form" scope="col">Form</th>
                        <th className="next" scope="col">Next</th>

                    </tr>
                </thead>
                <tbody>
                    {teams.map((team, index) =>
                        <tr key={team.id}>
                            <td className="position" >{index + 1}</td>
                            <td className="club">{team.name}</td>
                            <td className="played">{team.wins + team.draws + team.loses}</td>
                            <td className="won">{team.wins}</td>
                            <td className="drawn">{team.draws}</td>
                            <td className="lost">{team.loses}</td>
                            <td className="gf">{team.goal_scored}</td>
                            <td className="ga">{team.goal_concended}</td>
                            <td className="gd">11</td>
                            <td className="points">{team.points}</td>
                            <td className="form">GOOOD</td>
                            <td className="next">BEEOEOEOEOM</td>
                        </tr>)}

                </tbody>
            </table>
        </>
    )
}





export default Table;
