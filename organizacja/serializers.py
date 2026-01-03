from rest_framework import serializers
from .models import Czlonek, WidokBazyCzlonkow, Kierunek, Czlonekkierunek, Sekcja, Czloneksekcji, Czlonekprojektu, \
    Projekt, Partner, WidokPartnerow, OdpowiedziSlownik, Przychod, WidokBudzetu, Wydatek


# Moduł członków
class WidokBazyCzlonkowSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidokBazyCzlonkow
        fields = '__all__'


class CzlonekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Czlonek
        fields = ['id', 'imie', 'nazwisko', 'e_mail', 'indeks', 'telefon', 'opis']


class CzlonekKierunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Czlonekkierunek
        fields = '__all__'


class KierunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kierunek
        fields = '__all__'


class SekcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sekcja
        fields = '__all__'


class CzlonekSekcjiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Czloneksekcji
        fields = '__all__'


class ProjektSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projekt
        fields = '__all__'


class CzlonekProjektuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Czlonekprojektu
        fields = '__all__'

# Moduł partnerów
class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class WidokPartnerowSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidokPartnerow
        fields = '__all__'

class OdpowiedziSlownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = OdpowiedziSlownik
        fields = '__all__'


# Moduł budżetu
# Moduł Budżet
class PrzychodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Przychod
        fields = '__all__'


class WydatekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wydatek
        fields = '__all__'


class WidokBudzetuSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidokBudzetu
        fields = '__all__'