document.addEventListener('DOMContentLoaded', function () {
    const districts = {
        Kigali: ["Gasabo", "Kicukiro", "Nyarugenge"],
        Southern: ["Gisagara", "Huye", "Kamonyi", "Muhanga", "Nyamagabe", "Nyanza", "Nyaruguru", "Ruhango"],
        Western: ["Karongi", "Ngororero", "Nyabihu", "Nyamasheke", "Rubavu", "Rusizi", "Rutsiro"],
        Northern: ["Burera", "Gakenke", "Gicumbi", "Musanze", "Rulindo"],
        Eastern: ["Bugesera", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Nyagatare", "Rwamagana"]
    };

    const sectors = {
        Gasabo: [ "Bumbogo","Gatsata","Gikomero","Gisozi","Jabana","Jali","Kacyiru","Kimihurura","Kimironko","Kinyinya","Ndera","Nduba","Remera","Rusororo","Rutunga"],
        Kicukiro:["Gahanga","Gatenga","Gikondo","Kagarama","Kanombe","Kicukiro","Kigarama","Masaka","Niboye","Nyarugunga"],
        Nyarugenge: ["Gitega","Kanyinya","Kigali","Kimisagara","Mageragere","Muhima","Nyakabanda","Nyamirambo","Nyarugenge","Rwezamenyo"]
    };

    const cells = {
        "Gahanga": ["Kagasa", "Karembure", "Murinja", "Nyakabanda"],
        "Gatenga":["Gatenga", "Kanserege", "Kibabo", "Kigarama"],
        "Gikondo": ["Gikondo", "Kicukiro", "Kigarama", "Marembo"],
        "Kagarama": ["Kagarama", "Akabugu", "Kamashashi", "Kiyovu"],
        "Kanombe": ["Kanombe", "Karama", "Kabeza", "Nyarugunga"],
        "Kicukiro": ["Kicukiro", "Cyimo", "Gatenga", "Nyakabanda"],
        "Kigarama": ["Kigarama", "Kabeza", "Gatare", "Masaka"],
        "Masaka": ["Masaka", "Nyagahinga", "Nyamata", "Gatare"],
        "Niboye": ["Niboye", "Kagarama", "Kabeza", "Kicukiro"],
        "Nyarugunga": ["Nyarugunga", "Kamashashi", "Cyimo", "Akabugu"],
        
        
        
        
        "Gitega": ["Agatare", "Akabahizi", "Kora", "Nyabugogo"],
        "Kanyinya": ["Bweramvura", "Gahororo", "Munyinya", "Taba"],
        "Kigali": ["Kigali", "Kamukina", "Rugenge", "Rwesero"],
        "Kimisagara": ["Kimisagara", "Mikingo", "Muganza", "Nyabugogo"],
        "Mageragere": ["Gatenga", "Gasharu", "Kabuga", "Mageragere"],
        "Muhima": ["Muhima", "Nyabugogo", "Rugenge", "Akumunigo"],
        "Nyakabanda": ["Kabuye", "Mushimire", "Nyakabanda I", "Nyakabanda II"],
        "Nyamirambo": ["Rugarama", "Cyivugiza", "Gasharu", "Mumena"],
        "Nyarugenge": ["Kiyovu", "Muhima", "Nyabugogo", "Rwezamenyo"],
        "Rwezamenyo":["Kigondo", "Kora", "Rwezamenyo I", "Rwezamenyo II"],
        
        
        
        "Bumbogo": ["Gasabo", "Kamutwa", "Kinyaga", "Nyabikenke"],
        "Gatsata": ["Bugarama", "Karuruma", "Kavumu", "Nyamugari"],
        "Jabana" : ["Agatare", "Bukinanyana", "Gasagara", "Ngiryi"],
        "Gikomero": ["Buhiza", "Gasura", "Kagugu", "Nyabikenke"],
        "Gisozi": ["Gasave", "Kabuye", "Nyakabanda", "Rubungo"],
        "Kacyiru": ["Gacuriro", "Kamatamu", "Kinyinya", "Rukiri I"],
        "Kimihurura": ["Kimihurura", "Rugando", "Kibaza", "Kacyiru"],
        "Kimironko": ["Bibare", "Nyagatovu", "Nyabisindu", "Rukiri II"],
        "Kinyinya": ["Gasharu", "Gatare", "Gatwaro", "Murama"],
        "Ndera": ["Bushoki", "Cyaruzinge", "Gasharu", "Rukoma"],
        "Nduba": ["Gasanze", "Nyamweru", "Nyundo", "Rubungo"],
        "Remera": ["Gihogwe", "Kabeza", "Rukiri I", "Rukiri II"],
        "Rusororo": ["Gasagara", "Kabuga I", "Kabuga II", "Nyagahinga"],
        "Rutunga": ["Gasura", "Kagusa", "Kibenga", "Mataba"],
        
        
        
        
        
        
        
        
        
        
        
        // Add other cells similarly
    };

    const provinceSelect = document.getElementById('province');
    const districtSelect = document.getElementById('district');
    const sectorSelect = document.getElementById('sector');
    const cellSelect = document.getElementById('cell');
    const parkingServiceSelect = document.getElementById('parkingService');

    provinceSelect.addEventListener('change', function () {
        const province = this.value;
        districtSelect.innerHTML = '<option value="">Select District</option>';
        sectorSelect.innerHTML = '<option value="">Select Sector</option>';
        cellSelect.innerHTML = '<option value="">Select Cell</option>';
        districtSelect.disabled = true;
        sectorSelect.disabled = true;
        cellSelect.disabled = true;
        parkingServiceSelect.disabled = true;

        if (province) {
            districts[province].forEach(district => {
                const option = document.createElement('option');
                option.value = district;
                option.textContent = district;
                districtSelect.appendChild(option);
            });
            districtSelect.disabled = false;
        }
    });

    districtSelect.addEventListener('change', function () {
        const district = this.value;
        sectorSelect.innerHTML = '<option value="">Select Sector</option>';
        cellSelect.innerHTML = '<option value="">Select Cell</option>';
        sectorSelect.disabled = true;
        cellSelect.disabled = true;
        parkingServiceSelect.disabled = true;

        if (district) {
            sectors[district].forEach(sector => {
                const option = document.createElement('option');
                option.value = sector;
                option.textContent = sector;
                sectorSelect.appendChild(option);
            });
            sectorSelect.disabled = false;
        }
    });

    sectorSelect.addEventListener('change', function () {
        const sector = this.value;
        cellSelect.innerHTML = '<option value="">Select Cell</option>';
        cellSelect.disabled = true;
        parkingServiceSelect.disabled = true;

        if (sector) {
            cells[sector].forEach(cell => {
                const option = document.createElement('option');
                option.value = cell;
                option.textContent = cell;
                cellSelect.appendChild(option);
            });
            cellSelect.disabled = false;
        }
    });

    cellSelect.addEventListener('change', function () {
        parkingServiceSelect.disabled = false;
    });
});

