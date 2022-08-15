<p align="center">

  <a target="_blank">
    <img alt="amplication-logo" height="250" alt="Amplication Logo" src="./Images/logo.jpeg"/>
  </a>
</p>
<h3 align="center">
  <b>
    <a>
      Note Taking In Notion Using Voice Recognition
    </a>
  </b>
</h3>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" /> <!-- line breaker -->

## Abstract
It's a note taking program using speech recognition and storing notes in Notion 

## Features 

1. can take notes or todo in `Notion App` using Voice Recognition

## Tested OS
> Ubuntu 22.04 LTS

## How to use

- for using this program you need two things
  1. Notion Internal Integration Token
  2. Notion Database Id

- You can follow this [steps](https://developers.notion.com/docs/getting-started) to create ``Notion Internal Integration Token``, ``Notion Database and Notion Database Id``
  
- After creating notion database, create 3 columns and name as `Description`, `Date` and `Status`
![table](./Images/table.png)

### Columns Type
1. Description - `Title`
2. Date - `Date`
3. Status - `Text`

- After creating the table, `EXPORT` Integration Token and database id into the `Enviorment`
```bash
export NOTION_INTEGRATION_TOKEN=your_notion_internal_integration_token
export NOTION_DATABASE_ID=your_notion_database_id
```
##### Enter these commands in your terminal by replacing `token` and `database id`

- After exporing tokens and installing the requirements, `RUN` the python program
```bash
python main.py
```

### COMMANDS

- wake up commands 
> say `friday`, `hey friday` or `hi friday`
 
- to create notes
> say `create a note for me`



<br>
<div align="center">
<br>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" /> <!-- line breaker -->

<p>

 <a href="https://www.linkedin.com/in/adil-rahman-80b17a23a/"  >connect with me</a><br><br>
<a href="https://www.linkedin.com/in/adil-rahman-80b17a23a/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a> <a href="https://www.instagram.com/___i_am_iron_man/?hl=en" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a> <a href="https://twitter.com/bitbyte_1337" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="DEV.to"></a> <a href="https://medium.com/@adilrahman_1337" target="_blank"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="DEV.to"></a>

</p>
</div>

