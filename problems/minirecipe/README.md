# Mini-Recipe Project
**Öğrenci:** Merve Zeynep Beyazal (251478115)

Bu proje, komut satırı üzerinden yemek tariflerini yönetmeyi sağlayan basit bir uygulamadır.

## V1 -> V2 Sürüm Farkları

Proje geliştirme sürecinde V1 sürümünden V2 sürümüne geçerken yapılan temel iyileştirmeler aşağıdadır:

### 1. Yeni "Delete" Komutu
- **V1:** Tarifler sadece eklenebiliyor ve listelenebiliyordu, silme özelliği yoktu.
- **V2:** Kullanıcıların hatalı veya istenmeyen tarifleri ID numarası kullanarak silebilmesi için `delete <id>` komutu eklendi.

### 2. Gelişmiş Arama (Enhanced Search)
- **V1:** `search` komutu sadece malzemeler (ingredients) içinde arama yapıyordu.
- **V2:** Arama özelliği genişletilerek hem malzeme listesinde hem de tarif isimlerinde eşleşme bulacak şekilde güncellendi.

### 3. Güvenli Dosya İşlemleri (Refactoring)
- **V1:** Dosyalar `open()` ve `close()` yöntemleriyle manuel olarak açılıp kapatılıyordu.
- **V2:** Python'ın `with open` (context manager) yapısına geçildi. Bu sayede dosya işlemlerinde oluşabilecek hatalar ve kaynak sızıntıları engellenerek daha güvenli bir veri yönetimi sağlandı.

## Testler
Projenin doğruluğu hem V1 hem de V2 sürümleri için hazırlanan özel test dosyaları (`test-v1.py` ve `test-v2.py`) ile doğrulanmıştır.
