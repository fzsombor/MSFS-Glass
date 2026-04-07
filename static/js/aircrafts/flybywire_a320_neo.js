let AP_1;
let AP_2;
let AP_ATHR;
let AP_LOC_MODE;
let AP_EXPED_MODE;
let AP_APPR_MODE;
let AIRLINER_ICE_ENG1;
let AIRLINER_ICE_WING;
let AIRLINER_ICE_ENG2;
let AIRLINER_PROBE_HEAT;
let AIRLINER_WIPER_CPT;
let AIRLINER_LT_STROBE;
let AIRLINER_LT_NAVLOGO;
let AIRLINER_LT_TAXI;
let INSTRUMENT_LT_RWYTURN_IE_ID;

function getPlaneSimulatorData() {
    $.getJSON($SCRIPT_ROOT + '/ui', {}, function (data) {
        connected = data.connected;

        if (connected) {
            AP_1 = data.AP_1;
            AP_2 = data.AP_2;
            AP_ATHR = data.AP_ATHR;
            AP_LOC_MODE = data.AP_LOC_MODE
            AP_EXPED_MODE = data.AP_EXPED_MODE;
            AP_APPR_MODE = data.AP_APPR_MODE;
            AIRLINER_ICE_WING = data.WING_ANTI_ICE;
            AIRLINER_ICE_ENG1 = data.ENG1_ANTI_ICE;
            AIRLINER_ICE_ENG2 = data.ENG2_ANTI_ICE;
            AIRLINER_PROBE_HEAT = data.PROBE_HEAT;
            AIRLINER_WIPER_CPT = data.AIRLINER_WIPER_CPT;
            AIRLINER_LT_STROBE = data.AIRLINER_LT_STROBE;
            AIRLINER_LT_NAVLOGO = data.AIRLINER_LT_NAVLOGO;
            AIRLINER_LT_TAXI = data.AIRLINER_LT_TAXI;
            INSTRUMENT_LT_RWYTURN_IE_ID = data.INSTRUMENT_LT_RWYTURN_IE_ID;
        }
    });
    return connected;
}

function displayPlaneData() {
    checkAndUpdateButton("#ap-1", AP_1);
    checkAndUpdateButton("#ap-2", AP_2);
    checkAndUpdateButton("#a320-autothrottle", AP_ATHR);
    checkAndUpdateButton("#a320-loc-ap", AP_LOC_MODE);
    checkAndUpdateButton("#a320-exped-ap", AP_EXPED_MODE);
    checkAndUpdateButton("#a320-ice-wing", AIRLINER_ICE_WING, "Wing Anti Ice (On)", "Wing Anti Ice (Off)");
    checkAndUpdateButton("#a320-ice-eng1", AIRLINER_ICE_ENG1, "ENG1 Anti Ice (On)", "ENG1 Anti Ice (Off)");
    checkAndUpdateButton("#a320-ice-eng2", AIRLINER_ICE_ENG2, "ENG2 Anti Ice (On)", "ENG2 Anti Ice (Off)");
    checkAndUpdateButton("#a320-probe-heat", AIRLINER_PROBE_HEAT, "Probe/Window Heat (On)", "Probe/Window Heat (Off)");
    checkAndUpdateButton("#a320-cpt-wiper", AIRLINER_WIPER_CPT > 0 ? 1 : 0, "Pilot Wiper (" + (AIRLINER_WIPER_CPT === 1 ? "Slow" : "Fast") + ")", "Pilot Wiper (Off)");
    checkAndUpdateButton("#a320-light-strobe", AIRLINER_LT_STROBE < 2 ? 1 : 0, (AIRLINER_LT_STROBE === 1 ? "Auto" : "On") , "Off");
    checkAndUpdateButton("#a320-light-nav", AIRLINER_LT_NAVLOGO < 2 ? 1 : 0, (AIRLINER_LT_NAVLOGO === 1 ? "1" : "2") , "Off");
    checkAndUpdateButton("#a320-light-taxi", AIRLINER_LT_TAXI < 2 ? 1 : 0, (AIRLINER_LT_TAXI === 1 ? "Taxi" : "TO") , "Off");
    checkAndUpdateButton("#light-rwy", INSTRUMENT_LT_RWYTURN_IE_ID);
}

window.setInterval(function () {
    let isConnected = getPlaneSimulatorData();
    if (isConnected) {
        displayPlaneData();
    }
}, 200);
