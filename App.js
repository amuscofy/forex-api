import React, { useEffect, useState } from 'react';
import { StyleSheet, Text, View, FlatList, SafeAreaView } from 'react-native';

export default function App() {
  const [signals, setSignals] = useState([]);
  const [error, setError] = useState(null);  // State to hold any errors

  useEffect(() => {
    fetch('https://forex-api-m3vi.onrender.com/signals')
      .then(res => res.json())
      .then(data => {
        // Check if there's an error message in the response
        if (data && data.some(item => item.signal === "Error")) {
          setError("There was an issue fetching the signals. Please try again later.");
        } else {
          setSignals(data);
        }
      })
      .catch(err => {
        console.error(err);
        setError("Failed to fetch data. Please check your internet connection.");
      });
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
      {error ? (
        <Text style={styles.error}>{error}</Text>  // Show the error message if it exists
      ) : (
        <FlatList
          data={signals}
          keyExtractor={item => item.pair}
          renderItem={renderItem}
        />
      )}
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
  error: { color: 'red', textAlign: 'center', marginTop: 20 }
});
