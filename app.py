from flask import Flask, jsonify

app = Flask(__name__)

provinces = [
    {
        'province_id': "1",
        'province': "BALE",
        "chefLieu": "BOROMO",
        "departements": "Boromo, Bagassi, Fara, Pa, Pompoï, Poura, Siby, Oury, Yaho",
        "population": "169 543"
    },
    {
        "province_id": "2",
        "province": "BAM",
        "chefLieu": "Kongoussi",
        "departements": "Kongoussi, Bourzanga, Guibaré, Nasséré, Tikaré, Sabcé, Rollo, Rouko, Zitenga",
        "population": "212 295"
    },
    {
        "province_id": "3",
        "province": "BANWA",
        "chefLieu": "Solenzo",
        "departements": "Solenzo, Balavé, Kouka, Tansila, Sami, Sanaba",
        "population": "214 234"
    },
    {
        "province_id": "4",
        "province": "BAZEGA",
        "chefLieu": "Kombissiri",
        "departements": "Kombissiri, Doulougou, Ipelcé, Gaongo, Kayao,Toécé, Saponé.",
        "population": "214 450"
    },
    {
        "province_id": "5",
        "province": "BOUGOURIBA",
        "chefLieu": "Diébougou",
        "departements": "Diébougou, Dolo, Tiankoura, Bonddigui, Nioroniorro, Oronkua",
        "population": "76 444"
    },
    {
        "province_id": "6",
        "province": "BOULGOU",
        "chefLieu": "Tenkodogo",
        "departements": "Tenkodogo, Bané, Bagré, Béguédo, Bittou, Boussouma, Bissiga, Garango, Komtoéga, Niagho, "
                        "Zabré, Zoaga, Zonsé",
        "population": "415 414"
    },
    {
        "province_id": "7",
        "province": "BOUKIEMDE",
        "chefLieu": "Koudougou",
        "departements": "Koudougou, Bingo, Imasgo, Kindi, Kokologo, Nanoro, Niandiala, Pella, Poa, Ramongo, Sabou, "
                        "Siglé, Sourgou, Thiou, Soaw",
        "population": "421 083"
    },
    {
        "province_id": "8",
        "province": " COMOE",
        "chefLieu": "Banfora",
        "departements": "Banfora, Bérégadougou, Mangodara, Moussodougou, Niangoloko, Ouo, Sidéradougou, "
                        "Soubakaniédougou, Tiéfora",
        "population": "240 942"
    },
    {
        "province_id": "9",
        "province": "GANZOURGOU",
        "chefLieu": "Zorgho",
        "departements": "Zorgho, Boudry, Kogo, Méguet, Mogtédo, Salogo, Zam, Zoungou",
        "population": "257 707"
    },
    {
        "province_id": "10",
        "province": "GNAGNA",
        "chefLieu": "Bogandé",
        "departements": "Bogandé, Coalla, Bilanga, Liptougou, Mani, Pièla, Thion",
        "population": "307 386"
    }
]


@app.route('/')
def index():
    return 'Ma première application REST avec Flask!'


# fonction pour lister toutes les provinces

@app.route('/provinces', methods=['GET'])
def get_province():
    return jsonify({'Provinces': provinces})


# fonction pour lister une province avec son id
@app.route("/provinces/<int:province_id>", methods=['GET'])
def get_province_id(province_id):
    return jsonify({'province': provinces[province_id]})


# Fonction de création d'une province
@app.route("/provinces", methods=['POST'])
def create_province():
    province = {
        "province_id": "11",
        "province": "GOURMA",
        "chefLieu": "Fad N’Gourma",
        "departements": "Fada N’Gourma, Diabo, Diapangou, Matiacoali, Tibga, Yamba",
        "population": "221 956"
    }
    provinces.append(province)
    return jsonify({'Crée': province})


# Fonction de mise à jour d'une province
@app.route("/provinces/<int:province_id>", methods=['PUT'])
def update_province(province_id):
    provinces[province_id]['province'] = "Test"
    return jsonify({'province': provinces[province_id]})


# Fonction de suppression d'une province
@app.route("/provinces/<int:province_id>", methods=['DELETE'])
def delete_province(province_id):
    provinces.remove(provinces[province_id])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
