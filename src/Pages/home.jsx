import React from "react";
import Footer from "../Component/footer";

function Homepage() {
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
              <div class="about-item-text-1">

              </div>
              <div class="about-item-text-2">

              </div>
          </div>
        </div>
      </div>

      <Footer />
    </>
  );
}

export default Homepage;
