
/*

It's necessary to communicate the iframe with the Rocketbot view

*/

var message = {
    type: 'iframe',
    commands: {}
}
var SendMessage = function () {
    parent.postMessage(message, "*");
}
$('#serviceNames').on('change', function (e) {
    // e.data.printer
    message.commands['serviceName'] = $(this).val();
    message.commands['session'] = document.getElementById("ip").value
    SendMessage();
})
var eventMethod = window.addEventListener ? "addEventListener" : "attachEvent";
var eventer = window[eventMethod];
var messageEvent = eventMethod == "attachEvent" ? "onmessage" : "message";

// Listen to message from child window
eventer(messageEvent, function (e) {
    console.log(e)
    if (e.data && e.data.serviceName) {
        document.serviceNames_serviceName = e.data.serviceName.toLowerCase()
    }else{
        data = getDataFromRB({module_name:"CloudShore", command_name:"getMethods", data: "default"})
        .then(data => {
            console.log(data["serviceNames"])
            data = data.replaceAll("'", "\"")
            data = JSON.parse(`${data}`)
            data["serviceNames"].push("---- Select Option ----")
            serviceNames = data["serviceNames"]
            serviceNames.reverse()
            addOptions(serviceNames)
        })
    }
});

function getDataFromRB({module_name, command_name, data}) {
    let api = document.URL.split("module")[0]
    var formData = new FormData()
    let command_ = {
        "project": {
            "profile": {
                "name": module_name,
                "description": "",
                "version": "2020.12.30"
            },
            "vars": [
                {
                    "name": module_name + "_fake_var",
                    "data": "",
                    "type": "string",
                    "collapse": true,
                    "$$hashKey": "object:1204"
                }
            ],
            "commands": [
                {
                    "father": "module",
                    "command": `{\"module_name\":\"${module_name}\",\"module\":\"${command_name}\",\"var_name\":\"${module_name + "_fake_var"}\", \"session\":\"${data}\"}`,
                    "option": "",
                    "var": "",
                    "index": 0,
                    "group": "scripts",
                    "execute": 0,
                    "if": "",
                    "children": [],
                    "else": [],
                    "id": "50ad1403-a6d8-d1da-c654-77eba1a4830a",
                    "mode_live": true,
                    "getvar": "",
                    "extra_data": null,
                    "screenshot": "",
                    "execute_debbug": 0,
                    "img": ""
                }
            ],
            "ifs": []
        }
    }

    formData.append('info', JSON.stringify(command_))
    formData.append('db', "")
    var data = null
    return fetch(api + "execute", {
        method: "POST",
        body: formData,
    }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => {
            data = response.vars[0].data
            // return eval( '(' + data + ')')
            return data
        });
}