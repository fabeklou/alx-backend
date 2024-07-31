import redis from 'redis';
import { promisify } from 'util';
import express from 'express';

const app = express();
const port = 1245;

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

const getItemById = (id) => {
  const item = listProducts.find(
    (product) => product.itemId === parseInt(id));
  return item;
};

/** Redis client setup */
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

/** Reserve stock by itemId */
const reserveStockById = (itemId, stock) => {
  setAsync(`item.${itemId}`, stock);
}

/** Get current reserved stock by itemId */
const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock) : null;
};

/** Routes */
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    currentStock !== null
      ? currentStock
      : item.initialAvailableQuantity;

  res.json({ ...item, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity =
    currentStock !== null
      ? currentStock
      : item.initialAvailableQuantity;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: parseInt(itemId) });
  }

  await reserveStockById(itemId, currentQuantity - 1);
  res.json({ status: 'Reservation confirmed', itemId: parseInt(itemId) });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
