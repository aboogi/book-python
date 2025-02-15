const PREFIX = {
    0: "1.",
    1: "2.",
    2: "3.",
    3: "4.",
    4: "5.",
    5: "6.",
    6: "7.",
    7: "8.",
    8: "9.",
    9: "10.",
    10: "11.",
    11: "12.",
    12: "13.",
    13: "14.",
    14: "15.",
    15: "16.",
    16: "17."
};


document.addEventListener("DOMContentLoaded", () => {
    let chapters = document.querySelectorAll("nav.wy-nav-side p.caption");

    chapters.forEach((chapter, i) => {
        chapter.innerHTML = `${PREFIX[i]} ${chapter.innerHTML}`;
    });
});
