console.log("Merhaba Kodlama.io");

//değişken tanımları. Aslında js eski bir dil ve
//saf js de değişken tanımı için var kullanılır
/*var dolarDun = 9.20;
var dolarBugun = 9.50;
//js type safe değildir. Türünü double tanımlar isen daha sonra değiştirebilirsin.
dolarDun="Ankara"
console.log(dolarDun+" "+dolarBugun)
*/
//let ile tanımlama yapacağız. let bize ne sağlar ? 
//let ile blok içerisinde değişim yapmaz. Ama var da blok içerisinde global değişkeni değiştirir.

let dolarDun = 9.20;
let dolarBugun = 9.50;
{
    let dolarDun = 9.10;
}
console.log(dolarDun + " " + dolarBugun)

//const ile sabit tanımlama yapabilirsin. Birdaha değişmez. Sadece okunabilir.
const euroDun = 11.2;
console.log(euroDun)

//array
//değişken ismi camelCase tanımlanmalıdır.
//PascalCase tanımlama ise bu şekilde.
let konutKredileri = ["Konut Kredisi", "Emlak Konut Kredisi", "Kamu Konut Kredisi"];

console.log("<ul>")
for (let i = 0; i < konutKredileri.length; i++) {
    console.log("<li>" + konutKredileri[i] + "</li>")
}
console.log("</ul>")

console.log(konutKredileri)