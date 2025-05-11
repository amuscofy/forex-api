// App.js

import React, { useEffect, useState } from 'react';
import { StyleSheet, Text, View, FlatList, SafeAreaView } from 'react-native';

export default function App() {
  const [signals, setSignals] = useState([]);

  useEffect(() => {
    fetch('http://<YOUR_API_URL>/signals')  // replace with your deployed FastAPI endpoint
      .then(res => res.json())
      .then(setSignals)
      .catch(err => console.error(err));
  }, []);

  const getColor = (signal) => {
    if (signal === 'Buy') return 'green';
    if (signal === 'Sell') return 'red';
    return 'gray';
  };

  const renderItem = ({ item }) => (
    <View style={styles.card}>
      <Text style={styles.pair}>{item.pair}</Text>
      <Text style={{ color: getColor(item.signal), fontSize: 18 }}>{item.signal}</Text>
      <Text style={styles.info}>RSI: {item.rsi} | MACD: {item.macd}</Text>
      <Text style={styles.timestamp}>{item.timestamp}</Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.header}>📈 Forex Signals</Text>
      <FlatList
        data={signals}
        keyExtractor={item => item.pair}
        renderItem={renderItem}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff', paddingTop: 50 },
  header: { fontSize: 24, fontWeight: 'bold', textAlign: 'center', marginBottom: 20 },
  card: { padding: 15, margin: 10, backgroundColor: '#f9f9f9', borderRadius: 10, elevation: 3 },
  pair: { fontSize: 20, fontWeight: 'bold' },
  info: { marginTop: 5, color: '#444' },
  timestamp: { fontSize: 12, color: '#aaa', marginTop: 5 },
});
