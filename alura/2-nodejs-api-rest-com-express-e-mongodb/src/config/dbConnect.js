import mongoose from "mongoose";

mongoose.connect(
  "mongodb+srv://brcls:12345@cluster0.fimnewb.mongodb.net/node-express"
);

let db = mongoose.connection;

export default db;
