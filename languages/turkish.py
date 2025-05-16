# Copyright 2025 Said Emirhan Döke
# Licensed under the Apache License, Version 2.0
translations = {
    "ThresholdingFrame": "📌 Threshold Bilgisi\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır. Renkli görüntülerde de işlem yapılabilir ancak en iyi sonuçlar **gri seviyeli** görüntülerde alınır.\n"
        "Çıkış Görüntüsü: İkili görüntü (binary image) olarak döner\n\n"
        "• Threshold: 0 ile 255 arasında bir değerdir. Bu eşik değeri, görüntüdeki piksellerin ikili hale getirilmesinde kullanılır.\n\n"
        "• Threshold Type:\n"
        "  - Binary: Piksel değeri eşikten büyükse 255 (beyaz), küçükse 0 (siyah) yapılır.\n"
        "  - Binary Inverse: Piksel değeri eşikten büyükse 0 (siyah), küçükse 255 (beyaz) yapılır.\n\n",
        
    "GaborFilterFrame": "📌 Gabor Filtresi Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır. Renkli görüntülerde de işlem yapılabilir ancak en iyi sonuçlar **gri seviyeli** görüntülerde alınır.\n"
        "Çıkış Görüntüsü: Gabor filtresi uygulanmış gri seviyeli görüntü döner.\n\n"
        "• Ksize: Çekirdeğin (kernel) boyutu. Tek sayı ve pozitif olmalıdır. Örn: 3, 5, 7...\n"
        "• Sigma: Gauss dağılımının standart sapması. Tipik aralık: 1.0 - 10.0\n"
        "• Theta: Filtrenin yönü (radyan cinsinden). 0 ile pi arasında bir değerdir.\n"
        "• Lambda: Sinüzoidal bileşenin dalga boyu. Pozitif bir değerdir. Örn: 4.0\n"
        "• Gamma: En-boy oranı. Genellikle 0 ile 1 arasında olur. 1: dairesel, <1: eliptik yapı.\n"
        "• Phi: Faz kayması. 0 ile 2*pi arasında değer alabilir.\n\n"
        "🎯 Not: Gri seviyeli görsellerle daha iyi sonuç verir.",
        
    "MorphologicalFrame": "📌 Morfolojik İşlemler Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır. Renkli görüntülerde de işlem yapılabilir ancak en iyi sonuçlar **gri seviyeli** görüntülerde alınır.\n"
        "Çıkış Görüntüsü: Morfolojik işlemler uygulanmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• Kernel Size: Yapısal elemanın boyutudur. Pozitif ve tek sayı olmalıdır. Örn: 3, 5, 7...\n"
        "• Kernel Shape: Çekirdek şeklidir. Rectangular (dikdörtgen), Ellipse (elips), veya Cross (çapraz) olabilir.\n"
        "• Operations: Uygulanacak morfolojik işlemi seçin:\n"
        "  - Erode: Nesneleri küçültür.\n"
        "  - Dilation: Nesneleri genişletir.\n"
        "  - Opening: Gürültü temizleme (erode ardından dilation).\n"
        "  - Closing: Küçük boşlukları kapatma (dilation ardından erode).\n"
        "  - Gradient: Kenarları çıkarır (dilation - erode).\n"
        "  - Top Hat: Orijinal görüntü - Opening sonucu.\n"
        "  - Black Hat: Closing sonucu - Orijinal görüntü.\n"
        "• Iterations: İşlemin kaç kez uygulanacağını belirtir. Genellikle 1-5 arası kullanılır.\n\n"
        "🎯 Not: Gri seviyeli görüntülerle daha etkili sonuçlar elde edilir.",
        
    "GammaTransformFrame": "📌 Gamma Dönüşümü Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli ve renkli görüntülerde çalışır.\n"
        "Çıkış Görüntüsü: Gamma dönüşümü uygulanmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• Gamma Value: Görüntünün parlaklığını ayarlayan pozitif bir değerdir. Genellikle 0.1 ile 5.0 arasında olur.\n"
        "  - Gamma < 1: Görüntü kararmaya başlar (daha koyu).\n"
        "  - Gamma > 1: Görüntü aydınlanır (daha parlak).\n\n"
        "🎯 Not: Görüntüdeki kontrastı değiştirebilir, ancak aşırı değerler görsel bozulmalara yol açabilir.",
        
    "CannyEdgeDetectorFrame": "📌 Canny Kenar Algılama Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır.\n"
        "Çıkış Görüntüsü: Canny kenar algılama uygulanmış gri seviyeli görüntü döner.\n\n"
        "• Kernel Size: Canny algılama çekirdeğinin boyutudur. Pozitif ve tek sayı olmalıdır. Örn: 3, 5, 7...\n"
        "• Low Threshold: Canny algoritmasındaki düşük eşik değeridir. 0 ile 255 arasında olmalıdır.\n"
        "• Max Threshold: Canny algoritmasındaki yüksek eşik değeridir. 0 ile 255 arasında olmalıdır.\n"
        "• L2gradient: Kenar Gradyanının hesaplanmasında daha fazla hassasiyet için kullanılan Boolean parametresi. L2 normunun kullanılıp kullanılmayacağını belirtir.\n\n"
        "🎯 Not: Düşük eşik değeri, kenarları daha hassas bir şekilde tespit eder. Yüksek eşik değeri, sadece belirgin kenarları alır.\n\n",
        
    "HoughTransformFrame": "📌 Hough dönüşümü ile çember algılama parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır\n"
        "Çıkış Görüntüsü: Hough dönüşümü ile çember algılama uygulanmış **renkli** görüntü döner.\n\n"
        "• Dp: Hough dönüşümünde kullanılan çözünürlük parametresidir. Genellikle 1.0 veya daha büyük bir değer olmalıdır.\n"
        "• Minimum Distance: Tespit edilen daireler arasındaki minimum mesafedir. Pozitif bir tamsayı olmalıdır.\n"
        "• Param1: Canny kenar algılama algoritmasındaki yüksek eşik değeridir. 0 ile 255 arasında olmalıdır.\n"
        "• Param2: Dairelerin merkezinin bulunabilmesi için gereken eşik değeridir. 0 ile 100 arasında olmalıdır.\n"
        "• Minimum Radius: Tespit edilecek dairelerin minimum çapıdır.\n"
        "• Maximum Radius: Tespit edilecek dairelerin maksimum çapıdır.\n"
        "• Mark Color: Tespit edilen dairelerin işaretleneceği renk.\n"
        "🎯 Not: Dairelerin net bir şekilde tespit edilebilmesi için giriş görselinin yüksek kontrast ve net olması önerilir.",
        
    "GaussianBlurFrame": "📌 Gaussian Blur Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli veya gri seviyeli olabilir.\n"
        "Çıkış Görüntüsü: Gaussian bulanıklık uygulanmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• Kernel Size: Gaussian bulanıklık filtresinin çekirdek boyutudur. Pozitif ve tek sayı olmalıdır. Örn: 3, 5, 7...\n"
        "• Sigma_X: X ekseni boyunca standart sapma değeridir. Pozitif bir sayı olmalıdır.\n"
        "• Sigma_Y: Y ekseni boyunca standart sapma değeridir. Pozitif bir sayı olmalıdır.\n\n"
        "🎯 Not: Gaussian bulanıklık, görüntüdeki gürültüyü azaltmak ve pürüzsüzleştirmek için kullanılır.",
        
    "KitterIllingworthFrame": "📌 Kittler-Illingworth Optimum Eşik Değeri Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır.\n"
        "Çıkış Görüntüsü: Kittler-Illingworth yöntemi ile hesaplanan optimum eşik değeri döner. Bir önceki işlemin görüntüsü döner ancak gösterilmez.\n\n"
        "• Optimum Threshold: Kittler-Illingworth yöntemine dayalı olarak görüntüdeki optimum eşik değeri.\n"
        "• Kittler-Illingworth yöntemi, görüntü histogramındaki iki sınıfı (arka plan ve ön plan) ayıran eşik değerini bulur.\n"
        "• Bu yöntem, sınıfların varyanslarını dikkate alarak en düşük maliyeti veren eşik değerini belirler.\n\n"
        "🎯 Not: Kittler-Illingworth yöntemi, özellikle aydınlık ve karanlık bölgelerin net bir şekilde ayrıldığı görüntülerde daha iyi sonuç verir.",
        
    "DrawHistogramFrame": "📌 Görüntü Histogramı Çizimi Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli veya gri seviyeli görüntü olabilir.\n"
        "Çıkış Görüntüsü: Histogram grafiği döner. Bir önceki işlemin görüntüsü döner ancak gösterilmez.\n\n"
        "• Görüntü Histogramı: Görüntüdeki piksellerin renk yoğunluklarını gösteren bir grafiktir.\n"
        "• Histogram, görüntüdeki farklı renk yoğunluklarının dağılımını analiz etmek için kullanılır.\n"
        "• Bu işlem, her pikselin gri ton değeri için frekansları hesaplar ve bir histogram oluşturur.\n\n"
        "🎯 Not: Histogram analizi, kontrast, parlaklık ayarları veya görüntü iyileştirme tekniklerini belirlemek için faydalıdır.",
        
    "ColorConvertFrame": "📌 Renk Dönüşümü Parametreleri\n\n"
        "• RGB'den Grayscale'e: Renkli bir görüntüyü gri tonlara dönüştürür. Her pikselin gri ton değeri hesaplanır.\n"
        "• Grayscale'den RGB'ye: Gri tonlu bir görüntüyü renklendirilmiş (RGB) görüntüye dönüştürür. Ancak orijinal renk bilgisi kaybolur.\n"
        "• RGB'den HSV'ye: Renkli bir görüntüyü, renk (Hue), doygunluk (Saturation) ve parlaklık (Value) bileşenlerine ayırır.\n"
        "• HSV'den RGB'ye: HSV formatındaki bir görüntüyü, kırmızı-yeşil-mavi (RGB) formatına dönüştürür.\n\n"
        "🎯 Not: Görüntü işleme ve renk analizi için uygun renk dönüşümünü seçmek önemlidir.",
        
    "ResizeFrame": "📌 Görüntü Yeniden Boyutlandırma Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli veya gri seviyeli görüntü olabilir.\n"
        "Çıkış Görüntüsü: Yeniden boyutlandırılmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• Width (Genişlik): Görüntünün yeni genişliği. Pozitif bir tamsayı değeri olmalıdır.\n"
        "• Height (Yükseklik): Görüntünün yeni yüksekliği. Pozitif bir tamsayı değeri olmalıdır.\n\n"
        "🎯 Not: Görüntü boyutları değiştirilirken orijinal görüntünün en-boy oranı korunmaz, bu da distorsiyona neden olabilir.",
        
    "RotateFrame": "📌 Görüntü Döndürme Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli veya gri seviyeli görüntü olabilir.\n"
        "Çıkış Görüntüsü: Döndürülmüş gri seviyeli veya renkli görüntü döner.\n\n"
        "• Rotation Angle (Dönme Açısı): Görüntünün döneceği açı. Seçenekler: 90°, 180°, 270°.\n\n"
        "🎯 Not: Seçilen döndürme açısı, görüntüyü saat yönünde döndürür.",
        
    "FlipFrame": "📌 Görüntü Çevirme Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli veya gri seviyeli görüntü olabilir.\n"
        "Çıkış Görüntüsü: Çevrilmiş gri seviyeli veya renkli görüntü döner.\n\n"
        "• Flip Direction (Çevirme Yönü): Görüntünün hangi yönde çevrileceği. Seçenekler: Yatay (Horizontal), Dikey (Vertical), Her İki Yön (Both).\n\n"
        "🎯 Not: Yatay çevirme, görüntüyü soldan sağa ters çevirir; dikey çevirme, görüntüyü yukarıdan aşağıya ters çevirir. Her iki yön seçildiğinde, hem yatay hem de dikey olarak tersine döner.",
        
    "MedianBlurFrame": "📌 Median Blur (Medyan Bulanıklığı) Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli veya gri seviyeli görüntü olabilir.\n"
        "Çıkış Görüntüsü: Medyan bulanıklığı uygulanmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• Kernel Size (Çekirdek Boyutu): Median bulanıklık algoritmasında kullanılan çekirdek boyutudur. Genellikle tek sayılar (3, 5, 7 vb.) kullanılır.\n\n"
        "🎯 Not: Çekirdek boyutunu arttırmak, daha fazla bulanıklık sağlar, ancak detayların kaybolmasına da yol açabilir. Görüntüdeki gürültüleri yumuşatmak için uygundur.",
        
    "BilateralFilterFrame": "📌 Bilateral Filter (İki Taraflı Filtre) Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli veya gri seviyeli görüntü olabilir.\n"
        "Çıkış Görüntüsü: Bilateral filtre uygulanmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• Diameter: Filtreleme sırasında her pikselin çevresinde kullanılacak piksel komşuluğunun çapı. Pozitif bir tamsayı olmalıdır.\n"
        "• Sigma Color: Renk uzayındaki standart sapmadır. Bu değer arttıkça, benzer renklerdeki pikseller daha fazla etkilenir.\n"
        "• Sigma Space: Uzamsal koordinatlar arasındaki mesafeye göre olan standart sapmadır. Bu değer arttıkça, daha uzak pikseller filtreye dahil edilir.\n\n"
        "🎯 Not: Bilateral filtre, kenarları koruyarak gürültüyü azaltmak için idealdir. Bu nedenle kenar netliğinin korunması istenen görüntülerde tercih edilir.",
        
    "Filter2DFrame": "📌 filter2D Konvolüsyon İşlemi Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli veya gri seviyeli görüntü olabilir.\n"
        "Çıkış Görüntüsü: Konvolüsyon işlemi uygulanmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• 3x3 Kernel: Görüntü üzerine uygulanacak çekirdek (kernel) değerlerini ifade eder.\n"
        "  Bu değerler, konvolüsyon işleminde her pikselin komşularıyla nasıl birleştirileceğini belirler.\n"
        "  Örneğin, kenar algılama, bulanıklaştırma veya keskinleştirme işlemleri için farklı çekirdekler kullanılabilir.\n\n"
        "🎯 Not: Girdi görüntüsü net ve kontrastlı olursa konvolüsyon etkisi daha belirgin olur.\n"
        "      Kernel değerlerinin toplamı yüksekse görüntü aydınlanabilir; negatif değerler keskinleştirme sağlar.",
        
    "SobelFrame": "📌 Sobel Kenar Algılama Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli görüntülerde de işlem yapılabilir ancak en iyi sonuçlar **gri seviyeli** görüntülerde alınır.\n"
        "Çıkış Görüntüsü: Sobel kenar algılama uygulanmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• dx: x ekseni yönünde türev alınıp alınmayacağını belirtir. 1 ise x yönlü kenarları algılar.\n"
        "• dy: y ekseni yönünde türev alınıp alınmayacağını belirtir. 1 ise y yönlü kenarları algılar.\n"
        "• Kernel Size: Sobel filtresinde kullanılacak çekirdek boyutudur. Pozitif tek sayı (örneğin: 1, 3, 5) olmalıdır.\n\n"
        "🎯 Not: dx ve dy birlikte 1 olarak seçilirse hem yatay hem dikey kenarlar algılanır.",
        
    "ScharrFrame": "📌 Scharr Kenar Algılama Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır. Renkli görüntülerde de işlem yapılabilir ancak en iyi sonuçlar **gri seviyeli** görüntülerde alınır.\n\n"
        "Çıkış Görüntüsü: Scharr kenar algılama uygulanmış gri seviyeli veya renkli görüntü döner.\n"
        "• dx: x ekseni yönünde türev alınıp alınmayacağını belirtir. 1 seçilirse yatay kenarları algılar.\n"
        "• dy: y ekseni yönünde türev alınıp alınmayacağını belirtir. 1 seçilirse dikey kenarları algılar.\n\n"
        "🎯 Not: Scharr filtresi, özellikle küçük çekirdek boyutlarında (örneğin 3x3) Sobel filtresine göre daha hassas sonuçlar verir.",
        
    "LaplacianFrame": "📌 Laplace Kenar Algılama Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır. Renkli görüntülerde de işlem yapılabilir ancak en iyi sonuçlar **gri seviyeli** görüntülerde alınır.\n"
        "Çıkış Görüntüsü: Laplace kenar algılama uygulanmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• Kernel Size: Türevi alırken kullanılan çekirdek (kernel) boyutu. Tek sayı ve pozitif olmalıdır (örn. 1, 3, 5).\n"
        "Daha büyük değerler daha fazla kenar detayı çıkarabilir fakat aynı zamanda görüntüde bulanıklığa da yol açabilir.\n\n"
        "🎯 Not: Laplace operatörü, görüntüdeki ikinci türev bilgisini kullanarak kenarları simetrik olarak algılar.",
        
    "CornerHarrisFrame": "📌 Harris Köşe Algılama Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır. Renkli görüntülerde de işlem yapılabilir ancak en iyi sonuçlar **gri seviyeli** görüntülerde alınır.\n"
        "Çıkış Görüntüsü: Harris köşe algılama uygulanmış renkli görüntü döner.\n\n"
        "• Block Size: Her piksel için köşe algılamada kullanılan komşuluk boyutu.\n"
        "• Sobel Kernel Size: Türevlerin hesaplandığı Sobel filtresinin boyutu.\n"
        "• k Değeri: Harris denkleminde kullanılan serbest parametre (genellikle 0.04 - 0.06 arası).\n\n"
        "🟥 Yüksek cevap veren alanlar kırmızı ile işaretlenir, bu alanlar köşe içeriyor olabilir.",
        
    "GoodFeaturesToTrackFrame": "📌 Köşe Algılama: goodFeaturesToTrack\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır.\n"
        "Çıkış Görüntüsü: Köşe algılama uygulanmış renkli görüntü döner.\n\n"
        "• Max Corners: Algılanacak maksimum köşe sayısı.\n"
        "• Quality Level: Algılanan köşelerin minimum kalite eşiği (0 ile 1 arasında).\n"
        "• Min Distance: Algılanan köşeler arasındaki minimum mesafe (piksel cinsinden).\n\n"
        "🟢 Algılanan köşeler yeşil dairelerle gösterilir.",
        
    "AdaptiveThresholdFrame": "📌 Adaptif Eşikleme: adaptiveThreshold\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır.\n"
        "Çıkış Görüntüsü: Adaptif eşikleme uygulanmış gri seviyeli görüntü döner.\n\n"
        "• Max Value: Eşik üstündeki piksellere verilecek maksimum değer.\n"
        "• Adaptive Method: Yerel ortalama (Mean) veya Gauss ağırlıklı ortalama (Gaussian).\n"
        "• Threshold Type: Binary (beyaz-siyah) ya da Binary Inverted (siyah-beyaz).\n"
        "• Block Size: Yerel eşikleme için pencere boyutu (tek sayı ve >1 olmalı).\n"
        "• C: Ortalama değerden çıkarılacak sabit.\n\n"
        "📄 Bu işlem yalnızca gri seviye görüntülerde çalışır.",
        
    "OtsuThresholdFrame": "📌 Otsu Eşikleme: cv2.threshold + THRESH_OTSU\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır.\n"
        "Çıkış Görüntüsü: Optimum OTSU eşiği döner. Bir önceki işlemin görüntüsü döner ancak gösterilmez.\n\n"
        "• Max Value: Eşik üstü piksellere atanacak maksimum değer.\n"
        "• Threshold Type: Binary (beyaz-siyah) ya da Binary Inverted (siyah-beyaz).\n\n"
        "📄 Otsu yöntemi, ideal eşiği otomatik olarak belirler.\n"
        "📄 Sadece gri seviye görüntülerle çalışır.",
        
    "FindContoursFrame": "📌 Kenar Bulma (FindContours): cv2.findContours\n\n"
        "Giriş Görüntüsü: Öncesinde herhangi bir kenar algılama işlemi (Canny Edge Detection tavsiye edilir) uygulanmış gri seviyeli bir görüntü olmalıdır.\n"
        "Çıkış Görüntüsü: Kenarları bulunmuş renkli görüntü döner.\n\n"
        "• Retrieval Mode:\n"
        "   - RETR_EXTERNAL: Sadece dış konturları bulur.\n"
        "   - RETR_LIST: Tüm konturları düz bir liste olarak verir.\n"
        "   - RETR_TREE: Konturların hiyerarşisini verir.\n\n"
        "• Approximation Method:\n"
        "   - CHAIN_APPROX_SIMPLE: Gereksiz noktaları atar (daha hafif).\n"
        "   - CHAIN_APPROX_NONE: Tüm noktaları döndürür.\n\n",
        
    "DrawContoursFrame": "📌 Konturları Çizme (DrawContours): cv2.drawContours\n\n"
        "Giriş Görüntüsü: Öncesinde herhangi bir kenar algılama işlemi (Canny Edge Detection tavsiye edilir) uygulanmış gri seviyeli bir görüntü olmalıdır.\n"
        "Çıkış Görüntüsü: Kenarları bulunmuş renkli görüntü döner.\n\n"
        "• Kontur Kalınlığı:\n"
        "   - Kontur çizgilerinin kalınlığını belirtir.\n\n"
        "• Kontur Rengi:\n"
        "   - Seçilen renge göre konturlar çizilir.\n\n",
        
    "HoughLinesFrame": "📌 Hough Doğrusu Dönüşümü (HoughLines): cv2.HoughLines\n\n"
        "Giriş Görüntüsü: Öncesinde herhangi bir kenar algılama işlemi (Canny Edge Detection tavsiye edilir) uygulanmış gri seviyeli bir görüntü olmalıdır.\n"
        "Çıkış Görüntüsü:: Hough dönüşümü uygulanmış renkli görüntü döner.\n\n"
        "• Rho (Mesafe Çözünürlüğü):\n"
        "   - Çizgilerin depolandığı çözünürlük, genellikle piksel cinsindendir.\n\n"
        "• Theta (Açı Çözünürlüğü):\n"
        "   - Açı çözünürlüğü, genellikle radian cinsindendir.\n\n"
        "• Threshold (Eşik Değeri):\n"
        "   - Algılanan çizgilerin geçmesi gereken minimum puan sayısını belirtir.",
        
    "DFTFrame": "📌 Discrete Fourier Transform (DFT) Parametreleri\n\n"
        "• DFT Boyutu: DFT sonucu için görüntü boyutunu belirler. Görüntü gerekirse sıfırlarla doldurulurlar.\n"
        "• Sıfır Frekansını Ortaya Taşı: Eğer seçilirse, DFT sonucu sıfır frekans bileşeni spektrumun ortasına kaydırılır.\n\n"
        "🎯 Not: Görsel önce gri tonlamaya dönüştürülür, ardından DFT uygulanır ve sıfır frekans bileşeni belirtilen şekilde kaydırılır. Sonuç, genlik değerlerine dönüştürülüp normalleştirilir ve görüntülenir.",
        
    "IDFTFrame": "📌 Inverse Discrete Fourier Transform (IDFT) Parametreleri\n\n"
        "• IDFT Boyutu: IDFT sonucu için görüntü boyutunu belirler. Görüntü gerekirse sıfırlarla doldurulurlar.\n"
        "• Sıfır Frekansını Ortaya Taşı: Eğer seçilirse, IDFT sonucu sıfır frekans bileşeni spektrumun ortasına kaydırılır.\n\n"
        "🎯 Not: Görsel önce gri seviyeli olmalı ve Canny kenar algılama görüntüsü gereklidir. Sonrasında DFT işlemi yapılır ve IDFT uygulanarak görsel geri dönüştürülür.",
        
    "NumpyFFTFrame": "📌 Fourier Dönüşümü (FFT) ve Ters Fourier Dönüşümü (IFFT) Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır.\n\n"
        "Çıkış Görüntüsü: FFT veya IFFT uygulanmış gri seviyeli görüntü döner.\n"
        "• Dönüşüm Tipi: Görüntüye uygulanacak dönüşüm tipi seçilir: FFT (Fourier Dönüşümü) veya IFFT (Ters Fourier Dönüşümü).\n\n"
        "🎯 Not: Görsel float32 formatına çevrilir. Seçilen dönüşüm türüne göre işlem yapılır:\n"
        "  - FFT: Görüntü Fourier Dönüşümüne uygulanır ve sıfır frekansı merkeze kaydırılır. Sonuç, genlik spektrumu olarak normalleştirilip görüntülenir.\n"
        "  - IFFT: Görüntü önce Fourier Dönüşümüne sonra ise Ters Fourier Dönüşümüne tabi tutulur, bu işlemle görsel geri dönüştürülür ve normalleştirilir.",
        
    "EqualizeHistFrame": "📌 Histogram Eşitleme (EqualizeHist) Parametreleri\n\n"
        "Giriş Görüntüsü: Gri seviyeli bir görüntü olmalıdır.\n"
        "Çıkış Görüntüsü: Histogram eşitleme uygulanmış histogram tablosu ve görüntüsü döner.\n\n"
        "• Histogram Eşitleme: Görüntüdeki parlaklık değerlerinin dağılımını eşitlemek için histogram eşitleme uygulanır.\n\n"
        "🎯 Not: Histogram eşitleme, genellikle daha iyi görsel kontrastı elde etmek ve parlaklık seviyelerini dengelemek için kullanılır.",
        
    "CLAHEFrame": "📌 CLAHE (Contrast Limited Adaptive Histogram Equalization) Parametreleri\n\n"
        "Giriş Görüntüsü: Renkli veya gri seviyeli bir görüntü olabilir.\n"
        "Çıkış Görüntüsü: CLAHE uygulanmış gri seviyeli veya renkli görüntü döner.\n\n"
        "• Clip Limit: Kontrast sınırlamasının derecesini belirtir. Yüksek değerler daha keskin kontrastlar sağlar.\n"
        "• Tile Grid Size: Eşitleme işlemi için kullanılan bölgesel ızgaranın boyutunu belirtir. Küçük ızgaralar daha ayrıntılı sonuçlar verir.\n\n"
        "🎯 Not: CLAHE, özellikle aydınlatma koşullarının düzensiz olduğu görüntülerde kontrastı artırmak için kullanılır.",
}