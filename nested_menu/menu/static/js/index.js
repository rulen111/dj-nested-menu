const url = document.URL;
const selected = document.querySelectorAll(`a[href="${url}"]`);

for (let item of selected) {
    if (item.href == url) {
        item.style.background = "red";

        while (item.parentNode.tagName != "BODY") {
            const parent = item.parentNode;
            if (parent.tagName == "DETAILS") {
                parent.setAttribute("open", "");
            };

            item = parent;
        };
    };
};