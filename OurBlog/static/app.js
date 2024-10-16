console.log('app.js connected')
quote_section=document.getElementById('quote_section')

let getQuotes= async ()=>{
    try{
        // req=await axios.get('https://dummyjson.com/quotes')
        // sayings=await req
        // // console.log(sayings)
        // let quotes=sayings.data['quotes'][0];
        // let {quote,author}=quotes
        quote="Your heart is the size of an ocean. Go find yourself in its hidden depths."
        author="Rumi"
        createQuote(quote,author)

    }
    catch(e){
        console.log(e)
    }
    
}

function createQuote(quote,author){
    bq=document.createElement('blockquote')
    p=document.createElement('p')
    p.append(quote)

    cite=document.createElement('cite')
    cite.append(author)

    bq.appendChild(p)
    bq.appendChild(cite)
    quote_section.appendChild(bq)
}

getQuotes();