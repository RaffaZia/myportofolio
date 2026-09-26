Nama : Raffa Zia Arya putra

NPM : 2506619285

Kelas : PBP A

## Tugas 1

1. Pada Tutorial dan Tugas 1, saya menggunakan beberapa elemen semantik HTML5 seperti `<section>` dan `<article>`. Saya menggunakan `<section>` untuk membagi halaman menjadi beberapa bagian utama, yaitu Profile, Education, dan Experience. Sementara itu, saya menggunakan `<article>` untuk setiap informasi pendidikan dan pengalaman karena masing-masing informasi tersebut dapat dianggap sebagai satu unit informasi yang berdiri sendiri. Penggunaan elemen tersebut membantu saya membuat struktur HTML yang lebih terorganisir dan mudah dipahami sebelum mulai mengatur tampilannya menggunakan CSS. Saya juga merasa penggunaan elemen semantik membuat struktur website lebih jelas dibandingkan jika seluruh halaman hanya menggunakan `<div>`. Untuk membuat static web, struktur ini membantu saya memisahkan isi berdasarkan bagian-bagian yang memiliki tujuan berbeda sehingga lebih mudah dikembangkan ketika menambahkan section baru.

2. Tantangan yang saya temukan ketika membuat website responsive adalah menentukan bagaimana layout yang awalnya dibuat untuk desktop harus disesuaikan ketika ukuran layar menjadi lebih kecil. Pada tampilan desktop, bagian Profile menggunakan layout dengan dua kolom, yaitu informasi di sebelah kiri dan foto di sebelah kanan. Namun, jika layout tersebut dipertahankan pada layar yang lebih kecil, konten menjadi terlalu sempit. Oleh karena itu, saya menggunakan media query untuk mengubah layout menjadi satu kolom pada ukuran layar tertentu. Saya juga perlu menyesuaikan ukuran foto, navigasi, dan susunan informasi agar tetap nyaman dilihat pada perangkat mobile. Dari proses tersebut, saya belajar bahwa responsive design bukan hanya tentang mengecilkan ukuran elemen, tetapi juga menentukan kembali posisi dan prioritas setiap elemen sesuai dengan ukuran layar.

3. Salah satu keterbatasan yang saya rasakan dari static web adalah informasi di dalam website masih harus diperbarui secara manual melalui kode HTML. Misalnya, ketika ingin menambahkan pengalaman organisasi atau pendidikan baru, saya perlu mengubah isi HTML secara langsung. Website juga belum dapat menyimpan atau mengambil data secara dinamis karena belum menggunakan database maupun backend. Jika proyek ini dikembangkan lebih lanjut, saya ingin menambahkan sistem pengelolaan data untuk bagian Experience dan Education sehingga informasi dapat ditambahkan atau diperbarui tanpa harus mengubah struktur HTML secara langsung. Selain itu, saya juga tertarik menambahkan fitur seperti halaman project yang datanya dapat diperbarui secara dinamis dan sistem filter untuk membantu pengunjung melihat project berdasarkan kategori.

Dalam pengerjaan Tugas 1 ini, saya juga mencoba menggunakan elemen **`<article>`** ketika menyusun bagian Education dan Experience. Saya memilih elemen tersebut karena setiap riwayat pendidikan atau pengalaman memiliki informasi yang cukup lengkap dan dapat dipisahkan sebagai satu kesatuan, seperti nama institusi atau kegiatan, posisi/peran, dan tahun. Hal ini membuat struktur HTML lebih terorganisir dan nantinya memudahkan saya ketika memberikan styling yang berbeda pada setiap item menggunakan CSS.

Selama pengerjaan saya tidak menggunakan AI. Salah satu masalah yang saya temukan adalah ketika menambahkan section Education dan Experience, tampilan keduanya belum memiliki struktur dan tata letak yang sesuai karena CSS yang sebelumnya saya buat hanya mengatur bagian Profile. Saya kemudian memeriksa kembali struktur HTML dan CSS, lalu menambahkan class yang sesuai untuk setiap bagian seperti education-item, experience-item, dan section-heading. Saya juga mencoba menyesuaikan layout menggunakan CSS Grid agar beberapa bagian Experience dapat ditampilkan dalam dua kolom pada desktop dan satu kolom pada layar yang lebih kecil. Dalam proses pengerjaannya, saya lebih banyak menggunakan metode trial and error, yaitu dengan mencoba mengubah dan menyesuaikan kode yang sudah dibuat pada Tutorial 1 untuk melihat pengaruhnya terhadap tampilan website dan saya juga mencari referensi dari css documentation pada link berikut https://developer.mozilla.org/en-US/docs/Web/CSS dan website https://www.w3schools.com/ serta buku pegangan yang saya miliki. Dari proses tersebut, saya belajar untuk memahami fungsi dari setiap bagian kode melalui percobaan secara langsung, serta memahami bahwa ketika menambahkan section baru, struktur HTML dan CSS perlu disesuaikan agar keduanya dapat bekerja dengan baik.


## Tugas 2

1. Ketika pengguna membuka halaman portfolio, browser terlebih dahulu mengirimkan HTTP request ke URL yang dituju. Request tersebut diterima oleh Django dan diproses melalui `urls.py` pada project yang kemudian meneruskannya ke `urls.py` pada aplikasi `main`. Pada `main/urls.py`, URL tersebut dipetakan ke view yang sesuai menggunakan named route. View kemudian menjalankan logika yang diperlukan, termasuk mengambil data dari model menggunakan query Django ORM. Setelah data diperoleh, view memasukkannya ke dalam context dan meneruskannya ke template. Template kemudian menggabungkan struktur HTML dengan data dari context menggunakan Django Template Language. Hasil render tersebut dikembalikan oleh Django sebagai HTTP response sehingga halaman portfolio dapat ditampilkan pada browser. Alur ini sesuai dengan arsitektur MTV Django, di mana View menjadi penghubung antara Model dan Template.

2. Data untuk bagian portfolio sebaiknya disimpan pada model karena data tersebut dapat berubah tanpa harus mengubah struktur HTML secara langsung. Jika data ditulis secara hard-coded di dalam template, setiap perubahan atau penambahan data mengharuskan developer mengubah file HTML secara manual. Dengan menyimpan data pada model, template cukup mengambil data dari context dan menampilkannya menggunakan perulangan. Hal ini membuat kode lebih mudah dipelihara dan memungkinkan data dikelola melalui database. Selain itu, pemisahan antara data dan tampilan membuat pengembangan fitur menjadi lebih terstruktur karena perubahan pada data tidak perlu mengubah bagian presentation layer.

3. `makemigrations` dan `migrate` memiliki fungsi yang berbeda tetapi saling berkaitan. `makemigrations` digunakan untuk mendeteksi perubahan pada model di `models.py` dan membuat file migration yang berisi instruksi perubahan struktur database. Setelah itu, `migrate` digunakan untuk menerapkan migration tersebut ke database sehingga struktur database sesuai dengan model yang telah dibuat. Contohnya, ketika saya menambahkan model `Education` yang memiliki field `institution`, `degree`, `started_at`, dan `ended_at`, saya perlu menjalankan `python manage.py makemigrations` untuk membuat file migration baru. Setelah migration berhasil dibuat, saya menjalankan `python manage.py migrate` agar tabel `Education` benar-benar dibuat di database. Jika hanya menjalankan `makemigrations` tanpa `migrate`, file migration memang akan tersedia, tetapi perubahan struktur database belum diterapkan.

Deklarasi AI :

Selama pengerjaan tugas ini saya tidak menggunakan AI dalam proses implementasi kode. Saya mengerjakan setiap bagian secara mandiri dengan memahami struktur project dan mengikuti alur Model-View-Template (MTV) Django serta mengikuti langkah-langkah pada tutorial 2 yang saya sesuaikan lagi dengan section yang saya kerjakan. Salah satu hal yang menjadi tantangan dalam pengerjaan adalah mengubah bagian Education yang sebelumnya ditulis secara hard-coded menjadi data yang dapat diambil dari database. Saya perlu menentukan struktur model yang sesuai untuk menyimpan informasi seperti nama institusi, jenjang pendidikan, serta tahun mulai dan selesai. Setelah menentukan field yang diperlukan, saya menghubungkan model tersebut dengan view dan template agar data dapat ditampilkan secara dinamis menggunakan Django. Salah satu permasalahan yang cukup reflektif bagi saya adalah ketika menambahkan model Education, saya sempat mengalami error karena salah menuliskan parameter blank menjadi Blank. Saya kemudian membaca pesan error yang diberikan oleh Django dan memperbaiki penulisan parameter tersebut menjadi blank=True. Setelah itu, saya menjalankan makemigrations dan migrate untuk menerapkan perubahan model ke database. Hal tersebut membuat saya menyadari bahwa dalam proses pembuatan sebuah project web seperti ini dibutuhkan ketelitian dan fokus yang tinggi. Typo sedikit saja bisa menyebabkan kesalahan yang fatal. Memang tidak ada indikasi error pada vs code seperti garis kuning atau merah, namun hal tersebut berpotensi menimbulkan runtime error ketika kita akan migrasi models tersebut.

Saya juga melakukan pengecekan terhadap struktur models.py, views.py, urls.py, dan template untuk memastikan data Education dapat mengalir dari database hingga ditampilkan pada halaman website. Selain itu, saya menambahkan unit test untuk memastikan URL dapat diakses, data Education dapat ditampilkan ketika tersedia, serta pesan kondisi kosong muncul ketika belum terdapat data. Dari proses tersebut, saya belajar memahami hubungan antara Model, View, Template, dan URL dalam Django serta menjadi lebih terbiasa membaca pesan error dan mencari letak masalah secara mandiri.


## Tugas 3
1. Dengan Menggunakan `ModelForm` pada Django kita dapat membuat form berdasarkan model Django yang sudah dibuat. Dengan `ModelFrom` kita tidak perlu membuat setiap field form secara manual menggunakan HTML dan kemudian menangani proses penyimpanannya secara terpisah. Selain itu, penggunaan `ModelForm` juga membuat proses pengembangan jauh lebih efisien karena struktur form mengikuti model yang sudah ada. Selain itu, Django juga membantu validasi terhadap data yang dimasukkan sebelum data disimpan ke database.

Sementara itu penggunaan `{% csrf_token %}` wajib ditambahkan pada form yang melakukan request POST untuk melindungi aplikasi dari serangan CSRF. Dimana CSRF ini merupakan serangan dimana ketika pengguna yang sedang login dapat secara tidak sengaja mengirimkan request ke aplikasi melalui website lain. Django memberikan token unik pada setiap form. Ketika form dikirim, Django akan memastikan bahwa request berasal dari form yang dibuat oleh aplikasi kita

2. JSON dan XML sama sama dapat digunaan untuk melakukan pertukaran data antara aplikasi. Namun, JSON lebih banyak digunakan dalam pengembangan aplikasi web modern karena memiliki struktur yang lebih sederhana dan lebih ringkas. JSON menggunakan struktur yang mirip dengan object dan array pada JavaScript. Hal ini membuat JSON lebih mudah digunakan dalam aplikasi web, terutama ketika data perlu di proses menggunakan javaScript. Dibandingan dengan XML, JSON memiliki sintaks yang lebuh sederhana sehingga data yang dikirimkan cenderung lebh ringkas dan lebih mudah dibaca dan diproses.

3. Pada Tugas ini, data portofolio berupa experience disimpan dalam databse dan direpresentasikan menggunakan model Django experience. Untuk mengembalikan data tersebut dalam bentuk JSON. Langkah pertama, `Experience.objects.all()` digunakan untuk mengambil seluruh data Experience dari databse. Hasilnya berupa kumpulan object django. Kemudian, data tersebut diproses menggunakan `serializers.serialize("json", experience_list)` proses ini disebut **serialization**, yaitu proses mengubah object atau data yang direpresentasikan oleh model django menjadi format JSON. Serialization diperlukan karena object Django yang berasal dari database tidak dapat langsung dikirimkan sebagai response JSON. Data tersebut harus terlebih dahulu diubah menjadi format yang dapat dipahami dan diproses oleh client. Setelah proses serialization selesai, data JSOn dikembalikan menggunakan HttpResponse yang memberikan informasi kepada client bahwa response yang diterima memiliki format JSON. Kemudian JSOn tersebut juga digunakan kembali pada halaman experience melalui proses `deserialization`. Data JSON yang sebelumnya dibuat melalui serialization diubah kembali menjadi object django sebelum dikirimkan ke template. 

secara singkat alurnya Database -> django model -> serialization -> JSON -> deserialization -> django objects -> template -> halaman experience


### AI Disclosure

### Deskripsi Proyek

Tugas 3 merupakan pengembangan lanjutan dari website portofolio pribadi yang telah dibuat pada tugas sebelumnya menggunakan framework Django. Pada tugas ini, saya mengembangkan fitur `Experience` agar data pengalaman dapat dikelola secara dinamis melalui aplikasi.

Fitur yang dikembangkan meliputi penambahan data menggunakan `ModelForm`, menampilkan data dari database, mengubah data yang sudah ada, menghapus data, serta menyediakan endpoint JSON untuk data `Experience`. Data JSON tersebut kemudian digunakan kembali melalui proses deserialization sebelum ditampilkan pada halaman Experience.

Dalam pengerjaannya, saya melakukan penyesuaian terhadap struktur dari Tutorial 03 dengan menggunakan objek `Experience` yang sudah terdapat pada proyek saya, bukan menggunakan objek `Project` seperti contoh pada tutorial.

### Problem Solving

Saya tidak menggunakan AI untuk menulis, menghasilkan, atau menyelesaikan kode program pada Tugas 3. Implementasi kode, debugging, penyesuaian struktur tutorial dengan proyek, serta proses problem solving dilakukan secara mandiri berdasarkan materi perkuliahan, tutorial, dan dokumentasi yang digunakan dalam pengerjaan tugas.

Selama pengerjaan Tugas 3, terdapat beberapa bagian yang perlu saya pahami dan selesaikan secara mandiri.

**1. Menyesuaikan implementasi tutorial dengan struktur proyek**

Tutorial 03 menggunakan objek `Project`, sedangkan proyek saya menggunakan model `Experience`. Oleh karena itu, saya perlu menyesuaikan `ModelForm`, view, URL, template, dan proses JSON agar sesuai dengan field yang terdapat pada model `Experience`.

Saya menyelesaikannya dengan memahami hubungan antara model, form, view, URL, dan template terlebih dahulu, kemudian mengimplementasikan setiap bagian berdasarkan struktur proyek yang sudah dibuat pada tugas sebelumnya.

**2. Menggunakan kembali template form untuk create dan update**

Saya ingin menghindari pembuatan dua template yang berbeda untuk menambahkan dan mengubah Experience. Oleh karena itu, experience_form.html dibuat agar dapat digunakan untuk kedua kebutuhan tersebut.

Pada proses update, form diberikan instance dari Experience yang ingin diubah sehingga data sebelumnya dapat ditampilkan kembali pada form. Tampilan judul dan tombol juga dibuat menyesuaikan apakah form digunakan untuk menambahkan atau mengubah data.

**3. Memahami proses Serialization dan Deserialization**
Bagian JSON menjadi salah satu bagian yang perlu saya pahami karena data yang terdapat pada database berupa object Django tidak dapat langsung dikembalikan sebagai JSON.

Saya menggunakan proses serialization untuk mengubah object Experience menjadi data JSON pada endpoint /api/experience/. Setelah itu, pada view show_experience, data JSON tersebut diproses kembali menggunakan deserialization sehingga dapat digunakan sebagai object Django oleh template.

**4. Menghindari duplikasi CSS pada form**

Saat mengembangkan form untuk `Experience`, saya menyadari bahwa struktur dan kebutuhan styling form tersebut memiliki banyak kesamaan dengan form `Education` yang sudah dibuat sebelumnya. Jika setiap form memiliki styling yang ditulis secara terpisah, akan terjadi duplikasi CSS dan kode menjadi lebih sulit untuk dipelihara.

Untuk mengatasinya, saya menggunakan selector CSS yang bersifat umum dan dapat digunakan oleh kedua form. Styling untuk elemen seperti `input`, `textarea`, `select`, tombol submit, serta bagian action form dibuat agar dapat digunakan kembali oleh form `Education` maupun `Experience`.

Dengan pendekatan tersebut, ketika terdapat perubahan pada tampilan form, saya tidak perlu mengubah styling pada setiap halaman secara terpisah. Hal ini membuat kode CSS menjadi lebih reusable dan mengurangi duplikasi kode.

Sebagai contoh, styling form dibuat menggunakan selector yang dapat digunakan bersama:


.education-form input,
.education-form textarea,
.education-form select,
.experience-form input,
.experience-form textarea,
.experience-form select {
    /* styling yang sama */
}


## AI Diclosure Tugas 4

Saya tidak menggunakan AI untuk menulis, menghasilkan, atau menyelesaikan kode program pada Tugas 3. Implementasi kode, debugging, penyesuaian struktur tutorial dengan proyek, serta proses problem solving dilakukan secara mandiri berdasarkan materi perkuliahan, tutorial, dan dokumentasi yang digunakan dalam pengerjaan tugas.

### Deskripsi Proyek
Tugas 4 merupakan pengembangan lanjutan dari website portofolio pribadi yang telah dibuat pada tugas sebelumnya menggunakan framework Django. Pada tugas ini, saya menerapkan sistem authentication dan authorization untuk membatasi akses pengguna terhadap data portofolio.

Fitur yang dikembangkan meliputi penerapan role Editor menggunakan Django Group dan Permission, pembatasan akses terhadap fitur tambah, ubah, dan hapus data Experience, serta penerapan fitur star yang hanya dapat digunakan oleh pengguna yang sudah login. Selain itu, saya juga menerapkan pembatasan akses pada bagian Education agar pengguna dengan role Editor dapat mengubah data tanpa memiliki hak untuk menambah atau menghapus data.

Dalam pengerjaannya, saya melakukan penyesuaian terhadap struktur dari Tutorial 04 dengan menggunakan objek Experience dan Education yang sudah terdapat pada proyek saya.

### Problem Solving

**1. Menerapkan role Editor menggunakan Django Group dan Permission**
Saya perlu membuat role baru yaitu Editor yang memiliki hak untuk mengubah data, tetapi tidak dapat menambah atau menghapus data. Untuk menerapkannya, saya membuat Group Editor melalui Django Admin dan memberikan permission change_experience serta change_education.

**2. Menggunakan has_perm() untuk membatasi akses**
Salah satu bagian yang perlu saya pahami adalah perbedaan antara pengecekan is_superuser dan permission yang dimiliki pengguna. Sebelumnya, fitur edit hanya dapat digunakan oleh superuser. Dengan demikian, akses edit ditentukan berdasarkan permission yang dimiliki pengguna, sehingga superuser maupun pengguna yang termasuk Group Editor dapat mengubah data, sedangkan pengguna biasa tetap mendapatkan HTTP 403 Forbidden.

**3. Menyesuaikan tampilan berdasarkan hak akses**
Selain membatasi akses pada sisi server, saya juga menyembunyikan tombol aksi yang tidak dapat digunakan oleh pengguna. Sebagai contoh, tombol Edit ditampilkan kepada pengguna yang memiliki permission change_experience, sedangkan tombol Add dan Delete hanya ditampilkan kepada superuser. Hal ini membuat pembatasan akses diterapkan pada dua sisi, yaitu tampilan pada template dan validasi permission pada view.

**4. Menambahkan fitur Edit pada Education**
Terdapat kesalahan pada fitur education dimana education ini saya jadikan sebagai fitur yang disesuaikan untuk tutorial 3 sehingga saya lupa untuk menambahkan fitur edit pada section education. Pada bagian Education, sebelumnya data hanya dapat ditambahkan dan dihapus. Karena role Editor pada tugas ini harus dapat mengubah data, saya menambahkan fitur update_education serta menyesuaikan form dan URL agar dapat digunakan untuk proses edit. Permission change_education kemudian diberikan kepada Group Editor, sementara fitur tambah dan hapus tetap dibatasi untuk superuser.