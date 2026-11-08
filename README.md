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

Saya tidak menggunakan AI untuk menulis, menghasilkan, atau menyelesaikan kode program pada Tugas 4. Implementasi kode, debugging, penyesuaian struktur tutorial dengan proyek, serta proses problem solving dilakukan secara mandiri berdasarkan materi perkuliahan, tutorial, dan dokumentasi yang digunakan dalam pengerjaan tugas.

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


### Tugas 5
1. Debouncing adalah teknik untuk menunda eksekusi suatu fungsi sampai pengguna berhenti melakukan suatu aktivitas selama waktu tertentu. Pada fitur pencarian menggunakan AJAX, debouncing digunakan agar request ke server tidak dikirim setiap kali pengguna mengetik satu karakter. Sebagai contoh, ketika pengguna mengetik kata "Education", tanpa debouncing browser dapat mengirim request untuk setiap perubahan input seperti E, Ed, Edu, Educ, dan seterusnya. Hal ini dapat menyebabkan terlalu banyak request ke server. Dengan debouncing, request hanya dikirim setelah pengguna berhenti mengetik selama beberapa waktu, misalnya 300 milidetik. Dengan demikian, jumlah request yang dikirim menjadi lebih sedikit, server tidak menerima request yang tidak diperlukan, dan fitur pencarian menjadi lebih efisien serta responsif.Pada implementasi saya, debouncing diterapkan menggunakan setTimeout() dan clearTimeout() dengan delay 300 milidetik sebelum menjalankan fungsi fetchEducation().

2. fetch() merupakan fungsi asynchronous yang mengembalikan sebuah Promise. Keyword await digunakan untuk menunggu Promise tersebut selesai sebelum kode pada baris berikutnya dijalankan. Dengan demikian, hasil dari fetch() dapat langsung disimpan ke dalam variabel dan digunakan pada proses berikutnya.

Contohnya:
const response = await fetch(EDUCATION_ENDPOINT);
const result = await response.json();

Pada kode tersebut, program akan menunggu sampai proses fetch() selesai sebelum melanjutkan ke response.json(). Setelah itu, program juga menunggu sampai response berhasil diubah menjadi data JSON. Jika await tidak digunakan, fetch() akan langsung mengembalikan sebuah Promise, sementara kode berikutnya tetap dijalankan tanpa menunggu hasil dari request tersebut. Akibatnya, kita belum mendapatkan objek Response atau data JSON yang sebenarnya ketika ingin menggunakannya.
Hal ini juga sesuai dengan materi Tutorial 05 yang menjelaskan bahwa tanpa await, Promise tetap berjalan di belakang layar dan kode berikutnya langsung dieksekusi tanpa menunggu proses tersebut selesai.

3. Cross-Site Scripting (XSS) adalah serangan ketika penyerang menyisipkan kode JavaScript berbahaya ke dalam halaman web sehingga kode tersebut dapat dijalankan pada browser pengguna. Pada aplikasi Django, data yang ditampilkan secara langsung menggunakan template Django relatif lebih aman karena Django secara otomatis melakukan HTML escaping terhadap variabel yang ditampilkan menggunakan {{ }}. Contohnya, karakter < dan > akan diubah menjadi bentuk yang tidak dianggap sebagai tag HTML oleh browser.Sementara itu, ketika data diperoleh melalui AJAX, data tersebut diterima oleh JavaScript dalam bentuk JSON. Jika data tersebut kemudian langsung dimasukkan ke halaman menggunakan innerHTML, browser akan menganggap isi data tersebut sebagai HTML. Oleh karena itu, apabila data mengandung tag atau atribut berbahaya, kode tersebut dapat dieksekusi oleh browser.

Sebagai contoh, data seperti:
<img src="x" onerror="alert('XSS!')">

dapat menjadi berbahaya apabila langsung dimasukkan menggunakan innerHTML.
Untuk mencegah hal tersebut, pada implementasi saya saya membuat fungsi escapeHtml() dan melakukan escaping terhadap data sebelum dimasukkan ke dalam HTML. Dengan demikian, data dari server tetap ditampilkan sebagai teks dan tidak dieksekusi sebagai HTML atau JavaScript.

## AI Diclosure
Saya tidak menggunakan AI untuk menulis, menghasilkan, atau menyelesaikan kode program pada Tugas 5. Implementasi kode, debugging, penyesuaian struktur tutorial dengan proyek, serta proses problem solving dilakukan secara mandiri berdasarkan materi perkuliahan, tutorial, dan dokumentasi yang digunakan dalam pengerjaan tugas.

### Set-up Project
Pada Tugas 5, saya melanjutkan proyek website portofolio yang telah dibuat pada tutorial sebelumnya. Implementasi pada tugas ini berfokus pada penggunaan JavaScript untuk membuat halaman menjadi lebih interaktif dengan menerapkan AJAX menggunakan Fetch API.
Pada bagian Education, saya menyesuaikan implementasi dari fitur Experience agar data dapat ditampilkan secara dinamis melalui AJAX tanpa melakukan reload halaman. Saya juga menambahkan fitur pencarian, debouncing, modal untuk menambahkan data, AJAX POST, toast notification, serta validasi dan perlindungan terhadap XSS.
Selain itu, implementasi pada Tugas 5 tetap mempertahankan sistem autentikasi dan otorisasi dari Tugas 4. Oleh karena itu, fitur seperti tambah, edit, dan hapus Education tetap dibatasi berdasarkan hak akses pengguna.

### Deskripsi Project dan Problem Solving
**1. Menerapkan AJAX untuk menampilkan data Education**
Saya perlu menyesuaikan fitur Education agar data tidak lagi ditampilkan secara langsung melalui template Django, tetapi dapat dimuat secara dinamis menggunakan JavaScript dan AJAX. Untuk menerapkannya, saya membuat endpoint get_education_json yang mengembalikan data Education dalam bentuk JsonResponse. Pada sisi frontend, JavaScript menggunakan fetch() untuk mengambil data dari endpoint tersebut. Data JSON yang diterima kemudian digunakan untuk membuat elemen Education secara dinamis sehingga halaman dapat diperbarui tanpa melakukan reload.

**2. Menambahkan fitur pencarian dengan AJAX dan Debouncing**
Saya menambahkan fitur pencarian pada halaman Education agar pengguna dapat mencari data berdasarkan nama institusi atau program pendidikan. Search dilakukan dengan mengirimkan parameter query ke endpoint JSON dan melakukan filtering pada sisi server. Saya juga menerapkan teknik debouncing pada input pencarian. Dengan demikian, request AJAX tidak dikirim setiap kali pengguna mengetik karakter, tetapi hanya dikirim setelah pengguna berhenti mengetik selama beberapa saat. Hal ini mengurangi jumlah request yang dikirim ke server dan membuat fitur pencarian lebih efisien.

**3. Menambahkan loading, error, dan empty state**
Karena data Education sekarang dimuat secara asynchronous menggunakan AJAX, saya perlu menangani beberapa kemungkinan kondisi pada halaman. Saya menambahkan loading state ketika data sedang dimuat, error state ketika request gagal, dan empty state ketika tidak terdapat data yang sesuai dengan pencarian.Dengan adanya ketiga kondisi tersebut, pengguna mendapatkan informasi yang jelas mengenai status proses pengambilan data.

**4. Menambahkan fitur Add Education menggunakan AJAX**
Saya mengubah proses penambahan Education agar dapat dilakukan melalui modal tanpa melakukan reload halaman. Form Education ditampilkan menggunakan Popover API, kemudian ketika form disubmit, JavaScript mengirimkan data menggunakan fetch() dengan method POST. Setelah server berhasil menyimpan data, modal ditutup, toast success ditampilkan, dan daftar Education dimuat kembali menggunakan AJAX. Dengan demikian, Education baru dapat langsung muncul tanpa perlu melakukan refresh halaman.

**5. Menambahkan CSRF Token pada AJAX POST**
Karena proses penambahan Education menggunakan HTTP POST, saya perlu memastikan request tersebut tetap dilindungi oleh mekanisme CSRF Django. Saya mengambil CSRF token dari cookie kemudian mengirimkannya melalui header X-CSRFToken pada request fetch().
Dengan demikian, request AJAX tetap mengikuti mekanisme keamanan CSRF yang digunakan oleh Django. Tutorial 05 juga menekankan bahwa request POST melalui AJAX perlu mengirimkan CSRF token.

**6. Menambahkan validasi dan perlindungan XSS**
Saya menambahkan validasi pada EducationForm untuk memastikan data yang dimasukkan pengguna valid. Selain itu, saya juga menerapkan perlindungan XSS karena data Education sekarang ditampilkan melalui JavaScript menggunakan innerHTML.
Saya membuat fungsi escapeHtml() untuk melakukan escaping terhadap data sebelum dimasukkan ke dalam HTML. Hal ini diperlukan karena Django tidak lagi melakukan auto-escaping terhadap data yang sudah diterima oleh JavaScript melalui JSON. Dengan melakukan escaping, data berbahaya akan ditampilkan sebagai teks dan tidak dieksekusi sebagai HTML atau JavaScript.

### Tugas 6

## AI Diclosure Tugas 6

Saya tidak menggunakan AI untuk menulis, menghasilkan, atau menyelesaikan kode program pada Tugas 4. Implementasi kode, debugging, penyesuaian struktur tutorial dengan proyek, serta proses problem solving dilakukan secara mandiri berdasarkan materi perkuliahan, tutorial, dan dokumentasi yang digunakan dalam pengerjaan tugas.

## Set-up Project

Pada Tugas 6, saya melanjutkan pengembangan proyek website portofolio yang telah dibuat pada tutorial dan tugas sebelumnya. Implementasi pada tugas ini berfokus pada penggunaan Django REST Framework (DRF) untuk membangun REST API sehingga pengelolaan data pada website dapat dilakukan melalui endpoint API dengan format JSON.

Pada bagian Education dan Experience, saya melakukan migrasi dari endpoint JSON yang sebelumnya dibuat menggunakan Django `JsonResponse` menjadi endpoint REST API menggunakan Django REST Framework. Saya membuat serializer untuk masing-masing model, API views untuk menangani operasi CRUD, serta konfigurasi URL untuk mengakses endpoint API.

Selain itu, saya membuat custom permission class untuk mengatur hak akses pengguna berdasarkan role dan permission yang dimiliki. Implementasi ini tetap mempertahankan sistem autentikasi dan otorisasi dari tugas sebelumnya, sehingga operasi tertentu seperti menambahkan, mengubah, dan menghapus data hanya dapat dilakukan oleh pengguna yang memiliki hak akses sesuai ketentuan.

Pada sisi frontend, saya menyesuaikan implementasi JavaScript yang sebelumnya menggunakan Fetch API agar dapat berkomunikasi dengan endpoint DRF. Fitur seperti menampilkan data, pencarian, penambahan, pengubahan, penghapusan, dan pemberian star pada Experience tetap dipertahankan. Saya juga menambahkan pengujian API untuk memastikan setiap endpoint, validasi, autentikasi, otorisasi, dan perlindungan CSRF berjalan sesuai spesifikasi.

## Deskripsi Project dan Problem Solving

**1. Mengimplementasikan REST API menggunakan Django REST Framework**

Saya perlu mengubah mekanisme pengelolaan data Education dan Experience agar tidak lagi bergantung pada endpoint JSON biasa yang dibuat menggunakan Django `JsonResponse`. Untuk mengatasi hal tersebut, saya menggunakan Django REST Framework sebagai framework untuk membangun REST API.

Saya menambahkan konfigurasi `rest_framework` pada `INSTALLED_APPS`, kemudian membuat file `api_views.py` dan `api_urls.py` untuk mengatur API views dan endpoint yang tersedia. Saya juga mengatur URL API dengan prefix `/api/v1/` agar endpoint dapat diakses melalui struktur URL yang lebih terorganisasi.

Dengan implementasi ini, data Education dan Experience dapat diakses dan dikelola melalui endpoint REST API dengan menggunakan HTTP methods seperti GET, POST, PUT, PATCH, dan DELETE.

**2. Membuat Serializer untuk Model Education dan Experience**

Saya membuat `EducationSerializer` dan `ExperienceSerializer` pada file `serializers.py` menggunakan `ModelSerializer` dari Django REST Framework. Serializer berfungsi untuk mengubah instance model Django menjadi representasi data yang dapat dikirimkan dalam format JSON, serta melakukan deserialisasi dan validasi terhadap data yang diterima dari request API.

Pada `EducationSerializer`, saya menentukan field yang dapat diakses melalui API dan mengatur `id` sebagai read-only field. Sementara itu, pada `ExperienceSerializer`, saya menambahkan beberapa field tambahan seperti `category_display`, `is_ongoing`, `star_count`, dan `is_starred`.

Saya juga menambahkan validasi pada field `title` dan `description` menggunakan `strip_tags()` untuk menghilangkan tag HTML serta memastikan nilai yang dimasukkan tidak kosong setelah dibersihkan.

Penggunaan serializer membuat proses konversi dan validasi data lebih terstruktur dibandingkan harus menyusun dictionary secara manual pada setiap API view.

**3. Membuat API Views untuk Operasi CRUD**

Saya membuat API views untuk menangani operasi CRUD pada Education dan Experience. Implementasi dilakukan menggunakan function-based views dengan decorator `@api_view` dari Django REST Framework.

Pada endpoint list, saya menyediakan method GET untuk mengambil seluruh data dan POST untuk menambahkan data baru. Sementara itu, endpoint detail mendukung GET untuk mengambil detail data, PUT dan PATCH untuk memperbarui data, serta DELETE untuk menghapus data.

Saya menggunakan `get_object_or_404()` untuk mengambil objek berdasarkan ID atau UUID dan memberikan respons 404 apabila data tidak ditemukan. Selain itu, proses validasi request dilakukan melalui serializer menggunakan `is_valid(raise_exception=True)` sebelum data disimpan.

Dengan demikian, setiap operasi CRUD memiliki endpoint dan HTTP method yang sesuai dengan prinsip REST API.

**4. Menerapkan Perbedaan PUT dan PATCH**

Dalam implementasi endpoint detail Education dan Experience, saya menyediakan dua method untuk memperbarui data, yaitu PUT dan PATCH.

PUT digunakan untuk memperbarui representasi resource secara keseluruhan, sedangkan PATCH digunakan untuk memperbarui sebagian field saja. Untuk membedakan keduanya, saya menggunakan parameter `partial` pada serializer:

```python
serializer = ExperienceSerializer(
    experience,
    data=request.data,
    partial=request.method == "PATCH"
)
```

Dengan pengaturan tersebut, ketika request menggunakan PATCH, pengguna tidak harus mengirimkan seluruh field yang tersedia. Hal ini berguna ketika hanya ingin mengubah satu atau beberapa informasi Experience tanpa harus mengirimkan kembali seluruh data.

**5. Menerapkan Authentication dan Permission pada API**

Saya menerapkan `SessionAuthentication` pada endpoint API agar request dapat menggunakan sesi login Django yang sudah tersedia pada website. Selain autentikasi, saya juga membuat custom permission class pada `permissions.py` untuk mengatur hak akses terhadap operasi API.

Pada Education dan Experience, pengguna yang belum login maupun pengguna biasa hanya dapat melakukan operasi read-only. Superuser memiliki akses penuh terhadap operasi CRUD, sedangkan Editor dapat melakukan perubahan data melalui PUT dan PATCH apabila memiliki permission `change_education` atau `change_experience`.

Saya juga menerapkan permission `IsAuthenticated` secara khusus pada endpoint star Experience agar hanya pengguna yang sudah login yang dapat memberikan atau membatalkan star.

Pemeriksaan permission dilakukan pada sisi backend menggunakan custom permission class, bukan hanya dengan menyembunyikan tombol pada template frontend. Dengan demikian, request yang dikirim secara langsung ke endpoint API tetap diperiksa berdasarkan hak akses pengguna.

**6. Mengintegrasikan REST API dengan Frontend Menggunakan Fetch API**

Setelah endpoint API tersedia, saya menyesuaikan JavaScript pada halaman Education dan Experience agar menggunakan endpoint DRF. Sebelumnya, frontend menggunakan endpoint JSON yang dibuat menggunakan `JsonResponse`. Pada tugas ini, seluruh proses pengambilan dan pengiriman data disesuaikan dengan struktur respons serializer DRF.

Saya menggunakan Fetch API untuk mengirim request dengan HTTP method yang sesuai. Pada proses GET, data JSON yang diterima digunakan untuk membangun elemen HTML secara dinamis. Pada proses POST, PUT, PATCH, dan DELETE, JavaScript mengirimkan data ke endpoint API dan menangani respons dari server.

Saya juga menyesuaikan cara membaca struktur JSON karena respons DRF langsung berupa objek dengan field seperti `id`, `title`, `description`, dan `category`, bukan lagi struktur hasil Django serialization yang menggunakan `item.pk` dan `item.fields`.

Dengan perubahan ini, frontend tetap dapat menggunakan fitur yang telah dibuat sebelumnya tanpa harus melakukan reload halaman setiap kali data diambil atau dimodifikasi.

**7. Mempertahankan Fitur Search, Create, Update, dan Delete**

Saya mempertahankan fitur pencarian dan pengelolaan data yang sebelumnya sudah dibuat pada Education dan Experience. Fitur search dilakukan dengan mengirimkan parameter query ke endpoint API, kemudian proses filtering dilakukan pada sisi backend menggunakan ORM Django.

Pada Education, pencarian dilakukan berdasarkan nama institusi dan jenjang pendidikan. Sementara itu, pada Experience, pencarian dilakukan berdasarkan judul maupun deskripsi pengalaman.

Untuk fitur Create, saya menggunakan request POST melalui Fetch API dan menampilkan form melalui modal. Setelah data berhasil disimpan, modal ditutup, toast notification ditampilkan, dan daftar data diperbarui kembali.

Untuk fitur Update, saya menggunakan request PATCH pada endpoint detail. Sementara itu, fitur Delete menggunakan request DELETE sehingga data dapat dihapus melalui API tanpa menggunakan mekanisme penghapusan form POST biasa.

Pada proses upload thumbnail Experience, saya menggunakan `FormData` agar data file dapat dikirimkan melalui request multipart/form-data. Dengan demikian, fitur upload thumbnail tetap dapat digunakan setelah migrasi ke DRF.

**8. Mempertahankan Fitur Star pada Experience**

Selain operasi CRUD, saya juga mempertahankan fitur star pada Experience yang telah dibuat pada tugas sebelumnya. Saya menyediakan endpoint khusus untuk mengelola star dengan method POST.

Pada API view `experience_star`, sistem memeriksa apakah pengguna sudah memberikan star terhadap Experience tersebut. Jika sudah, star akan dihapus. Jika belum, pengguna akan ditambahkan ke relasi `starred_by`.

Untuk menampilkan informasi star pada frontend, saya menambahkan `star_count` dan `is_starred` pada `ExperienceSerializer`. Dengan demikian, frontend dapat menampilkan jumlah star dan menentukan apakah tombol yang ditampilkan adalah Star atau Unstar berdasarkan status pengguna yang sedang login.

**9. Menerapkan CSRF Protection pada Request API**

Karena API menggunakan `SessionAuthentication`, request yang mengubah data tetap harus mengikuti perlindungan CSRF Django. Oleh karena itu, saya tetap mengambil CSRF token dari cookie menggunakan fungsi `getCookie()` dan mengirimkannya melalui header `X-CSRFToken` pada request Fetch API yang mengubah data.

Penerapan ini dilakukan pada request POST, PATCH, dan DELETE yang menggunakan sesi autentikasi Django. Untuk request yang mengirimkan file, saya menggunakan `FormData` dan tidak menetapkan header `Content-Type` secara manual agar browser dapat mengatur boundary multipart/form-data secara otomatis.

Dengan demikian, integrasi REST API tetap mempertahankan mekanisme perlindungan CSRF yang disediakan oleh Django.

**10. Menambahkan Automated API Testing**

Untuk memastikan API berjalan sesuai spesifikasi, saya menambahkan pengujian otomatis pada file `tests_api.py` menggunakan Django TestCase dan fasilitas pengujian dari Django REST Framework.

Pengujian dilakukan terhadap endpoint Education dan Experience, meliputi pengambilan data, pencarian, penambahan, perubahan, penghapusan, validasi input, autentikasi, otorisasi, dan penanganan method yang tidak diizinkan.

Saya juga menguji skenario CSRF, termasuk request tanpa token dan request dengan token yang valid. Pengujian ini membantu memastikan bahwa perlindungan CSRF benar-benar diterapkan pada request yang menggunakan autentikasi sesi.

Hasil pengujian menunjukkan bahwa seluruh 23 test berhasil dijalankan tanpa kegagalan. Dengan demikian, implementasi API Education dan Experience telah memenuhi skenario pengujian yang dibuat.

### Pertanyaan Reflektif

**1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta kapan masing-masing sebaiknya digunakan!**

REST (*Representational State Transfer*) merupakan suatu architectural style yang digunakan untuk merancang sistem terdistribusi, khususnya web API. REST mengatur bagaimana client berinteraksi dengan resource yang tersedia pada server melalui interface yang konsisten. Dalam REST, setiap resource memiliki identitas berupa URI atau URL dan dapat dimanipulasi menggunakan HTTP methods seperti GET, POST, PUT, PATCH, dan DELETE. REST juga memiliki beberapa prinsip, seperti client-server architecture, stateless communication, cacheability, uniform interface, dan layered system. Mengembalikan data dalam format JSON saja belum cukup untuk menyebut suatu API sebagai RESTful karena JSON hanya merupakan format representasi data. Sebuah API juga perlu memperhatikan prinsip dan batasan arsitektur REST, seperti penggunaan resource yang jelas, HTTP methods sesuai tujuan operasinya, serta komunikasi yang stateless. Sebagai contoh, API yang hanya mengembalikan JSON tetapi menggunakan satu endpoint untuk seluruh operasi tanpa memperhatikan semantik HTTP methods belum tentu dapat dikatakan RESTful.

Perbedaan PUT dan PATCH terletak pada cara keduanya memperbarui resource. PUT digunakan untuk mengganti representasi resource secara keseluruhan, sehingga client umumnya perlu mengirimkan seluruh field yang diperlukan. Sementara itu, PATCH digunakan untuk melakukan perubahan sebagian terhadap resource, sehingga client cukup mengirimkan field yang ingin diperbarui. Contohnya, ketika ingin memperbarui seluruh informasi Education seperti institution, degree, started_at, dan ended_at, PUT dapat digunakan. Namun, ketika hanya ingin mengubah degree tanpa mengubah informasi lainnya, PATCH lebih sesuai digunakan.

**2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan `JsonResponse` seperti pada Tutorial 05?**

Serializer pada Django REST Framework berfungsi untuk mengubah data dari model atau objek Python menjadi representasi yang dapat dikirimkan melalui API, seperti JSON. Serializer juga menangani proses deserialisasi, yaitu mengubah data yang diterima dari request menjadi data Python yang dapat diproses dan disimpan ke database. Selain itu, serializer menyediakan mekanisme validasi data sebelum data disimpan. Pada tugas ini, saya menggunakan `ModelSerializer` untuk model Education dan Experience agar field model dapat dikonversi secara otomatis menjadi field serializer. Saya juga dapat menentukan field yang boleh diakses, mengatur read-only field, serta menambahkan validasi khusus pada field tertentu. Dibandingkan merakit dictionary secara manual menggunakan `JsonResponse` seperti pada Tutorial 05, penggunaan serializer memiliki beberapa keuntungan. Pertama, proses konversi data menjadi JSON menjadi lebih terstruktur dan tidak perlu dilakukan secara manual untuk setiap field. Kedua, serializer menyediakan validasi input sehingga data yang diterima dapat diperiksa sebelum disimpan. Ketiga, serializer memudahkan pengaturan field yang dapat dibaca maupun diubah melalui API.

Dengan demikian, penggunaan serializer membuat implementasi API menjadi lebih konsisten, mudah dipelihara, dan mengurangi kebutuhan untuk menulis kode konversi serta validasi secara manual.

**3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan `permission class` di server, bukan hanya dengan menyembunyikan tombol di template?**

Autentikasi (*authentication*) merupakan proses untuk mengidentifikasi siapa pengguna yang melakukan request. Pada Django REST Framework, autentikasi dilakukan melalui authentication class, seperti `SessionAuthentication`, yang memanfaatkan sesi login Django untuk mengenali pengguna yang mengirimkan request. Sementara itu, otorisasi (*authorization*) merupakan proses untuk menentukan tindakan apa saja yang boleh dilakukan oleh pengguna yang sudah terautentikasi. Pada Django REST Framework, otorisasi dapat diatur menggunakan permission class.

Pada tugas ini, saya menggunakan `SessionAuthentication` untuk autentikasi dan membuat custom permission class untuk mengatur hak akses terhadap endpoint Education dan Experience. Sebagai contoh, Superuser memiliki akses penuh terhadap operasi CRUD, sedangkan Editor hanya dapat melakukan perubahan data apabila memiliki permission yang sesuai. Pemeriksaan hak akses harus dilakukan pada server menggunakan permission class karena frontend tidak dapat dijadikan mekanisme keamanan utama. Menyembunyikan tombol seperti Add, Edit, atau Delete pada template hanya memengaruhi tampilan antarmuka pengguna. Pengguna masih dapat mengirimkan request secara langsung melalui browser, API client, atau tools lainnya tanpa harus menekan tombol yang tersedia pada halaman.

Oleh karena itu, server tetap harus memeriksa autentikasi dan permission pada setiap request yang membutuhkan pembatasan akses. Dengan demikian, pengguna tidak dapat melakukan operasi yang tidak diizinkan meskipun mereka mencoba mengakses endpoint secara langsung.

**4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai `SessionAuthentication`! Mengapa test yang memakai `force_authenticate` tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?**

CSRF (*Cross-Site Request Forgery*) merupakan serangan yang memanfaatkan autentikasi pengguna yang masih aktif pada suatu website untuk mengirimkan request yang tidak diinginkan. Ketika API menggunakan `SessionAuthentication`, browser akan mengirimkan session cookie secara otomatis pada request ke server yang sesuai. Hal tersebut dapat menimbulkan risiko apabila terdapat website lain yang mencoba mengirimkan request menggunakan sesi pengguna yang masih aktif. Oleh karena itu, request yang mengubah data, seperti POST, PUT, PATCH, dan DELETE, tetap memerlukan perlindungan CSRF.  Pada tugas ini, saya mengambil CSRF token dari cookie menggunakan fungsi JavaScript `getCookie()` dan mengirimkannya melalui header `X-CSRFToken` ketika melakukan request yang mengubah data. Dengan demikian, Django dapat memverifikasi bahwa request tersebut memiliki token CSRF yang valid.

Sementara itu, `force_authenticate` pada pengujian Django REST Framework digunakan untuk memaksa suatu request dianggap berasal dari pengguna tertentu tanpa menjalankan proses autentikasi normal. Karena mekanisme autentikasi yang sebenarnya dilewati, pengujian yang hanya menggunakan `force_authenticate` tidak cukup untuk membuktikan bahwa perlindungan CSRF pada `SessionAuthentication` berjalan dengan benar. Untuk menguji perlindungan CSRF, pengujian perlu menggunakan mekanisme session authentication yang sebenarnya dengan CSRF checking diaktifkan. Dengan begitu, test dapat memverifikasi bahwa request tanpa token CSRF ditolak dan request dengan token CSRF yang valid dapat diproses sesuai hak akses pengguna.


