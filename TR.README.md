# ABC Analizi Uygulaması
# Giriş
ABC Analizi, malzeme yönetiminde yaygın olarak kullanılan bir envanter kategorizasyon yöntemidir. Seçici Stok Kontrolü olarak da bilinir. Envanterdeki ürünler, önemlerine göre A, B ve C olmak üzere üç kategoriye ayrılır. 'A' ürünleri en önemli olarak kabul edilir, 'B' ürünleri daha az önemli ve 'C' ürünleri en az öneme sahiptir.

Bu uygulama, belirli bir ürün seti ve bunların fiyatları ile miktarları üzerinde ABC Analizi yapmak için tasarlanmıştır. Tkinter kütüphanesi kullanılarak oluşturulan bir grafiksel kullanıcı arayüzü (GUI) kullanır ve matplotlib kullanarak grafikler oluşturur.

# Uygulamayı nasıl kullanırız
Uygulama başlatıldığında, "Ürün Adı", "Birim Fiyatı", "Miktar" ve "Toplam Fiyat" olarak adlandırılmış dört sütun içeren bir pencere görüntülenecektir. Ayrıca "Satır Ekle" ve "Hesapla" olarak adlandırılmış iki düğme bulunmaktadır.

Bir ürün için veri girmek için ilk satırdaki ilgili alanları doldurun:

Ürün Adı: Ürünün adını girin.
Birim Fiyatı: Ürünün birim fiyatını girin.
Miktar: Ürünün miktarını girin.
Toplam Fiyat: Toplam fiyatı doğrudan girebilir veya boş bırakabilirsiniz. Boş bırakılırsa, Birim Fiyatı * Miktar olarak hesaplanacaktır.
Daha fazla ürün eklemek için "Satır Ekle" düğmesine tıklayın. Bu, ek ürün bilgilerini girmeniz için yeni bir satır oluşturacaktır.

Tüm ürün bilgilerini girdikten sonra, "Hesapla" düğmesine tıklayın. Uygulama ABC Analizi yapacak ve şunları yapacaktır:

Toplam fiyatları ve birikimli toplamı gösteren bir grafik görüntülenecektir.
Ürün adını, toplam fiyatı, birikimli toplamı, birikim yüzdesini ve grubu (A, B veya C) gösteren bir tablo içeren yeni bir pencere açılacaktır.
Ana pencereyi kapatıp uygulamayı sonlandırabilirsiniz.

# Bağımlılıklar
Python
pandas
matplotlib
tkinter

# Amaç
Bu uygulama, envanter yöneticileri, küçük işletme sahipleri ve bir ürün seti üzerinde ABC Analizi yapmak isteyen herkes için faydalıdır. En çok değeri katkıda bulunan ürünleri anlamakta yardımcı olur ve envanter kontrolü ve yönetimi konusunda bilinçli kararlar almayı sağlar.

Lütfen bu uygulamanın eğitim amaçlı olduğunu ve profesyonel kullanım için ek özellikler ve doğrulama gerektirebileceğini unutmayın.




