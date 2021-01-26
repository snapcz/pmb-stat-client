import React, {useState} from "react";
import { useHistory } from 'react-router-dom'
import Footer from "../Component/footer";
import {Modal, Container, Row, Col} from 'react-bootstrap'

function Homepage() {
  const [show, setShow] = useState(false);
  const history = useHistory();

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const redir = () => {
      history.push("/unpar")
  }

  return (
    <>
      <div id="home">
        <div class="home-item-container">
          <div class="about-text">
            <div class="about-title">Tentang Website </div>
            <div class="about-content">
              Website Informasi Statistik Data Kegiatan Penerimaan Mahasiswa
              Baru UNPAR merupakan website yang ditujukan untuk memberikan
              informasi statistik dan insight bagi pengunjung terkait hal-hal
              yang kiranya dapat membantu penyusunan strategi promosi.
            </div>
          </div>
          <div class="about-img">
            <img id="web-img" src="./3156627.jpg" />
          </div>
        </div>

        <div class="home-item-container">
          <div class="about-img">
            <img id="dev-img" src="./3255469.jpg" />
          </div>
          <div class="about-text">
            <div class="about-title">Tentang Developer </div>
            <div class="about-content">
              Website ini dibangun oleh sekelompok mahasiswa Teknik Informatika
              UNPAR, sebagai tugas untuk pemenuhan matakuliah Proyek Sistem
              Informasi 2.{" "}
            </div>
          </div>
        </div>

        <div class="home-item-container-2">
          <div class="about-text-2">
            <div class="about-title">Tentang Konten Website</div>
            <div class="about-content-2">
              Kami membagi 2 pandangan dalam menyusun alur informasi dari
              kegiatan PMB UNPAR untuk menampilkan informasi dan insight dari
              peserta yang mengikuti kegiatan ini.
            </div>
          </div>
          <div class="about-item">
            <div class="about-item-text-1 left-rad">
              <div class="about-choice">
                <span class="about-number">1 </span> pandangan analisis secara
                menyeluruh dari level universitas
              </div>
            </div>
            <div class="about-item-text-2" onClick={redir}>
              <div>UNPAR</div>
            </div>
          </div>
          <div class="about-item">
            <div class="about-item-text-2" onClick={handleShow}>
              <div>JURUSAN</div>
            </div>
            <div class="about-item-text-1 right-rad">
              <div class="about-choice">
                <span class="about-number">2 </span> pandangan analisis secara
                menyeluruh dari level jurusan program studi.
              </div>
            </div>
          </div>
          <div class="about-text-2 m-30">
            <div class="about-content-2">
              Pengunjung dipersilahkan untuk memilih diantara kedua alur
              pandangan analisis ini. Namun untuk pilihan kedua, kami hanya
              menyediakan alur informasi untuk jurusan Informatika UNPAR saja.
            </div>
          </div>
        </div>
      </div>

      <Modal className="home-dialog" show={show} onHide={handleClose}>
        <Modal.Header className="home-header">
          <Modal.Title className="home-title">Jurusan</Modal.Title>
        </Modal.Header>
        <Modal.Body className="home-body">
            <Container>
              <Row>
                <Col className="prodi-choice-col">Ekonomi Pembangunan</Col>
                <Col className="prodi-choice-col">Manajemen</Col>
                <Col className="prodi-choice-col">Akuntansi</Col>
              </Row>
              <Row>
                <Col className="prodi-choice-col">Ilmu HUkum</Col>
                <Col className="prodi-choice-col">Ilmu Administrasi Publik</Col>
                <Col className="prodi-choice-col">Ilmu Administrasi Bisnis</Col>
              </Row>
              <Row>
                <Col className="prodi-choice-col">Ilmu Hubungan Internasional</Col>
                <Col className="prodi-choice-col">Teknik Sipil</Col>
                <Col className="prodi-choice-col">Arsitektur</Col>
              </Row>
              <Row>
                <Col className="prodi-choice-col">Ilmu Filsafat</Col>
                <Col className="prodi-choice-col">Teknik Industri</Col>
                <Col className="prodi-choice-col">Teknik Kimia</Col>
              </Row>
              <Row>
                <Col className="prodi-choice-col">Teknik Elektro</Col>
                <Col className="prodi-choice-col">Matematika</Col>
                <Col className="prodi-choice-col">Fisika</Col>
              </Row>
              <Row style={{justifyContent: 'space-around'}}>
                <Col className="prodi-choice-col">Informatika</Col>
                <Col className="prodi-choice-col">Manajemen Perusahaan</Col>
              </Row>
            </Container>
        </Modal.Body>
      </Modal>

      <Footer />
    </>
  );
}

export default Homepage;
