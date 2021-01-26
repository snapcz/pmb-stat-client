import React, { useState } from "react";
import Footer from "../Component/footer";
import { Container, Row, Col, Button } from "react-bootstrap";
import Map from "../Component/map";
import Navbar from "../Component/navbar";

function UnparPage() {
  const [state, setState] = useState(null);

  return (
    <>
      <Navbar />
      <Container fluid className="ext-btm">
        <Row>
          <Col id="tentang">
            <div>
              <h2>Tentang Jalur PMDK</h2>
              <p>
                Jalur Penerimaan PMDK merupakan salah satu jalur tes masuk yang
                disediakan oleh UNPAR. Peserta yang mendaftar melalui jalur ini
                umumnya hanya perlu menyertakan rapor nilai kelas X dan XI
                selama mengikuti jenjang SMA, dan memilih program studi apa yang
                ingin diambil oleh peserta tersebut. Kelulusan peserta akan
                dilihat dari faktor nilai rapor peserta, beserta dengan
                kesesuaian nilai mata pelajaran peserta pada program studi yang
                dipilih.
              </p>
            </div>
          </Col>
          <Col>
            <img className="chart-img" src="./trend_year.PNG" />
          </Col>
        </Row>
        <Row className="mt">
          <Col xs={7}>
            <div className="map_main">
              <div className="title">
                PETA SEBARAN TOTAL PARTISIPAN PMDK UNPAR 2013-2018
              </div>
              <div className="map_container">
                <Map showTable={setState} />
              </div>
              <span>
                <div className="subtext-title">
                  <h2>
                    Tentang Peta <br />
                    Sebaran Peserta
                  </h2>
                </div>
                <div className="subtext-body">
                  Peta sebaran peserta memberikan informasi dalam bentuk visual
                  peta terhadap sebaran peserta dari segi provinsi hingga kota
                  dalam jalur masuk tertentu.
                </div>
              </span>
            </div>
          </Col>
          <Col xs={4}>
            <div>
              <p>
                Interaksi yang dapat dilakukan:
                <ol>
                  <li>
                    {" "}
                    Drag/Zoom, untuk mengganti daerah yang ditampilkan /
                    memperbesar wilayah agar dapat meliaht pin kota
                  </li>
                  <li>
                    Hover daerah provinsi/pin kota, memunculkan informasi nama
                    provinsi/kota dan banyak peserta dari provinsi/kota
                    tersebut.
                  </li>
                  <li>
                    Single-click daerah provisi, menambahkan provinsi tersebut
                    disebuah line-chart yang menunjukkan informasi trend peserta
                    di provinsi tersebut. Daerah provinsi yang di-click kemudian
                    akan berganti warna (menunjukkan bahwa data trend provinsi
                    tersebut sedang berada di line-chart). Bila daerah di klik
                    kembali maka akan menghilangkan warna aktif sekaligus data
                    trend provinsi tersebut dari line-chart.
                  </li>
                  <li>
                    Double-cllick daerah provinsi, menampilkan daftar kota yang
                    ada di provinsi tersebut beserta jumlah peserta yang berasal
                    dari kota tesebut dalam bentuk bar-chart.
                  </li>
                  <li>
                    Single-click pin kota, menambahkan kota tersebut disebuah
                    line-chart yang menunjukkan informasi trend peserta di kota
                    tersebut. Pin kota yang di-click kemudian akan berganti
                    warna (menunjukkan bahwa data trend kota tersebut sedang
                    berada di line-chart). Bila daerah di klik kembali maka akan
                    menghilangkan warna aktif sekaligus data trend kota tersebut
                    dari line-chart.
                  </li>
                  <li>
                    Double-click pin kota, memunculkan tabel atau mengganti isi
                    tabel mengenai data sekolah beserta jumlah peserta sekolah
                    pada jalur pendaftaran yang dipilih.
                  </li>
                </ol>
              </p>
            </div>
          </Col>
        </Row>
        <Row className="mt">
          <Col className="centered">
            <img src="./trend_city.PNG" />
            <div className="button-cnt">
              <Button>+</Button>
              <Button>-</Button>
            </div>
          </Col>
          <Col className="centered">
            <img src="./top_city.PNG" />
          </Col>
        </Row>
        <Row className="mt">
          <Col xs={7}>
            <div className="tabel-main">
              <div className="title">Daftar Partisipan PMDK di Kota XXXX</div>
              <div>
                <img src="./tabel.PNG" />
              </div>
              <div className="button-cnt">
                <Button>Perbaharui</Button>
              </div>
            </div>
          </Col>
          <Col xs={4}>
            <div>
              <h2 className="centered">
                Tentang Tabel <br /> Daftar Partisipan
              </h2>
              <p>
                Daftar Partisipan PMDK di Kota Bandung merupakan tabel yang
                mengandung daftar sekolah-sekolah di kota Bandung dengan total
                partisipan jalur PMDK dari sekolah tersebut.
                <br />
                <br />
              </p>
              <p>
                Penjelasan setiap atribut/kolom:
                <ol>
                  <li>Sekolah, berisi nama sekolah</li>
                  <li>
                    Total Partisipan, berisi jumlah peserta yang mendaftar dari
                    sekolah tersebut
                  </li>
                  <li>
                    Total Partisipan Lulus, berisi jumlah peserta yang lulus
                    jalur PMDK dari sekolah tersebut
                  </li>
                  <li>
                    Total Daftar Ulang, berisi jumlah partisipan yang mendaftar
                    ulang setelah dinyatakan lulus pada jalur PMDK.
                  </li>
                </ol>
              </p>
              <br />
              <p>
                Aksi yang dapat dilakukan pada tabel:
                <ol>
                  <li>Sekolah, berisi nama sekolah</li>
                  <li>
                    Meng-klik baris: menampilkan detail sebaran program studi
                    pilihan peserta di sekolah tersebut dalam bentuk pie chart.
                  </li>
                  <li>
                    Checkbox: pengguna dapat memilih beberapa sekolah untuk di
                    checklist, kemudian menekan tombol perbaharui untuk
                    menampilkan trend total partisipan jalur PMDK
                    sekolah-sekolah tersebut.
                  </li>
                </ol>
              </p>
            </div>
          </Col>
        </Row>
        <Row className="mt">
          <Col xs={7}>
            <div id="long-chart-cnt">
              <div id="img1">
                <img src="./trinitas_pie.jpg" />
              </div>
              <div id="img2">
                <img src="./trinitas_trend.PNG" />
              </div>
              <div id="img3">
                <img src="./trinitas_boxplot.jpg" />
              </div>
            </div>
          </Col>
          <Col xs={4}>
            <h2 className="centered">Tentang Data Peserta</h2>
            <p>
              Data Peserta di SMU XXXXXXXXX merupakan field yang berisikan:
              <ol>
                <li>
                  pie-chart, digunakan untuk menunjukan persentase persebaran
                  pilihan Program Studi dari SMU XXXXX pada kegiatan PMDK UNPAR
                  di tahun XXXX.
                </li>
                <li>
                  line-chart, menunjukan trend Peserta PMDK di SMU XXXXXXXX
                  setiap tahun-nya.
                </li>
              </ol>
            </p>
            <br />
            <p>
              Aksi yang dapat dilakukan:
              <ol>
                <li>
                  Single-click daerah pie chart, menunjukan Ringkasan Data Nilai
                  Mata Pelajaran Peserta PMDK Tahun XXXX pada Program studi yang
                  di click. dalam bentuk box-plot.
                </li>
              </ol>
            </p>
          </Col>
        </Row>
      </Container>
      <Footer />
    </>
  );
}

export default UnparPage;
