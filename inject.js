let path = document.location.pathname;

if (typeof action !== "undefined" && Number(action) === 1) {
    if (path.endsWith('/userPage/userCenter')) {
        window.location.replace('https://hk.sz.gov.cn:8118/passInfo/detail');
    }
    if (path.endsWith('/passInfo/detail')) {
        window.location.replace("https://hk.sz.gov.cn:8118" + document.getElementsByClassName('orange button')[targetIndex].getAttribute('href'));
    }

    // user info
    username = 'ef5100126'
    password = 'huo520123'

    if (path.endsWith('/userPage/login')) {
        document.getElementById('input_idCardNo').value = username
        document.getElementById('input_pwd').value = password
    }


    if (path.endsWith('/passInfo/confirmOrder')) {
        document.getElementsByClassName('order-info')[0].style = 'display:none;';
        document.getElementById('TencentCaptcha').style = 'height:10rem;';
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

    document.getElementsByClassName("mask").remove()
    document.getElementsByClassName("winpop").remove()
} else {
    setInterval(function () {
        window.location.reload()
    }, 60 * 1000);
}