import React from 'react'
import { useHistory } from 'react-router-dom'

function Landing() {
    let history = useHistory();

    const redir = () => {
        history.push("/home")
    }

    return (
        <>
            <div id="welcome">Selamat datang di Website Informasi,</div>
            <div id="title">
                Statistik Data Kegiatan <br />
                Penerimaan Mahasiswa Baru <br />
                Universitas Katolik Parahyangan
            </div>

            <div id="btn-continue">
                <div id="text">
                    Continue
                </div>
                <div id="click" onClick={redir}>
                    <div id="chevron">
                        <i class="fas fa-chevron-right"></i>    
                        <i class="fas fa-chevron-right"></i>
                    </div>
                </div>
            </div>

            <img id="unpar" src='./Logo_UNPAR.png'/>
        </>
    )
}
export default Landing;