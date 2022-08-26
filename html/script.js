function addOptions(serviceNames) {
    var select = document.getElementById("serviceNames")
    document.querySelectorAll("#serviceNames option").forEach(option => option.remove())
    for (serviceName of serviceNames) {
        var opt = document.createElement('option');
        opt.value = serviceName;
        opt.innerHTML = serviceName;
        select.appendChild(opt);
        if (serviceName.toLowerCase() == document.serviceNames_serviceName) {
            opt.selected = true
        }
    }

}

ipInput = document.getElementById("ip")
ipInput.addEventListener("change", e=>{
    data = getDataFromRB({module_name:"CloudShore", command_name:"getMethods", data:e.target.value})
    .then(data => {
        console.log(data["serviceNames"])
        data = data.replaceAll("'", "\"")
        data = JSON.parse(`${data}`)
        data["serviceNames"].push("---- Select Option ----")
        serviceNames = data["serviceNames"]
        serviceNames.reverse()
        addOptions(serviceNames)
    })
})

