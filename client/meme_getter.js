/**
 * Main JS file
 */

const acc_username = "jshado";
const acc_password = "q&#RqmycL=7Hu@6e";

// Get all templates
let allMemes = [];
async function getTemplates() {
	const raw = await fetch("https://api.imgflip.com/get_memes");
	const json = await raw.json();
	const data = await json.data.memes;

	// for (const [i, meme] of data) {
	// 	const url = "";

	// 	const getData = await fetch("https://api.imgflip.com/caption_image");
	// }

	allMemes = data;

	return data;
}

async function displayMemes() {
	const data = await getTemplates();
	const DIV = document.getElementById("core");

	// Display images
	for (const [i, temp] of data.entries()) {
		let str = `<img src="${temp.url}" title="#${temp.id}: ${temp.name}" width="500" height="500" onClick="copyToClipboard('!meme ${temp.id}')">`;
		DIV.innerHTML += str;
	}
}
displayMemes();

function search(str) {
	const DIV = document.getElementById("core");
	DIV.innerHTML = "";

	for (const [i, meme] of allMemes.entries()) {
		if (
			meme.name.toLowerCase().includes(str.toLowerCase()) ||
			meme.id
				.toString()
				.toLowerCase()
				.includes(str.toLowerCase())
		) {
			let str = `<img src="${meme.url}" title="#${meme.id}: ${meme.name}" width="500" height="500" onClick="copyToClipboard('!meme ${meme.id}')">`;
			DIV.innerHTML += str;
		}
	}
}

function copyToClipboard(str) {
	const el = document.createElement("textarea");
	el.value = str;
	document.body.appendChild(el);
	el.select();
	document.execCommand("copy");
	document.body.removeChild(el);
	window.alert("Meme copied! " + str);
}
