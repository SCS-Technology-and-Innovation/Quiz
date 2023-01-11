const a = 7;
const c = 5;
const m = 1097;
const s = 8;
const n = 100; 

let x = s;
for (let i = 0; i < n; i++) {
    x = (a * x + c) % m;
    console.log(x);
}

