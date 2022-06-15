// user info
username = 'ef5100126'
password = 'huo520123'

let path = document.location.pathname;

const now = new Date()
let timeNow = now.getHours();
let minuteNow = now.getMinutes();

if ((timeNow === 9 || timeNow === 10) && (minuteNow === 59 || minuteNow === 0)) {
    if (path.endsWith('/userPage/userCenter') || path.endsWith('/error/index') || document.title === '403') {
        window.location.replace('https://hk.sz.gov.cn:8118/passInfo/detail');
    }
    if (path.endsWith('/passInfo/detail') || path.endsWith('/error/index') || document.title === '403') {
        window.location.replace("https://hk.sz.gov.cn:8118" + document.getElementsByClassName('orange button')[targetIndex].getAttribute('href'));
    }
} else {
    setInterval(function () {
        window.location.reload()
    }, 30 * 1000);
}

Element.prototype.remove = function () {
    this.parentElement.removeChild(this);
}

NodeList.prototype.remove = HTMLCollection.prototype.remove = function () {
    for (let i = this.length - 1; i >= 0; i--) {
        if (this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
}

if (path.endsWith('/userPage/login')) {
    document.getElementById('input_idCardNo').value = username
    document.getElementById('input_pwd').value = password
}

if (path.endsWith('/passInfo/confirmOrder')) {
    document.getElementById('TencentCaptcha').click()
}

document.getElementsByClassName("mask").remove()
document.getElementsByClassName("winpop").remove()